from collections import deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # [Change 1] letters as a set → O(1) membership instead of
        # scanning a list for every character
        letters = {char for word in words for char in word}

        # [Change 2] neighbor collections are sets → O(1) duplicate-edge
        # checks; indegree initialized for ALL letters up front
        # (this also fixes the missing-unconstrained-letters bug from earlier)
        graph = {char: set() for char in letters}
        indegree = {char: 0 for char in letters}

        # [Change 4 — biggest structural change]
        # The entire checklist / small_words / small_order suffix-slicing
        # machinery is gone. Instead, compare each ADJACENT pair of words
        # exactly once and extract at most one edge per pair.
        # No word[1:] copies → single O(total_chars) pass.
        for first, second in zip(words, words[1:]):
            found_difference = False
            for c1, c2 in zip(first, second):
                if c1 != c2:
                    if c2 not in graph[c1]:      # set lookup, O(1)
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    found_difference = True
                    break
            # prefix rule: "abc" before "ab" is invalid
            # (this also naturally handles the repeated-first-letter
            # cycle case — it just becomes a cycle in the graph)
            if not found_difference and len(first) > len(second):
                return ""

        # [Change 3] queue-based Kahn's algorithm → O(V + E),
        # no repeated full scans, no rebuilding key lists,
        # no popping from indegree mid-iteration
        queue = deque(char for char in letters if indegree[char] == 0)
        path = []

        while queue:
            parent = queue.popleft()
            path.append(parent)
            for child in graph[parent]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        # cycle detection: if not all letters made it out, there's a cycle
        if len(path) != len(letters):
            return ""

        # [Change 5] join instead of repeated string concatenation.
        # Note: no more "letters not in path" loop needed at all —
        # unconstrained letters start at indegree 0 and flow through
        # the queue like everything else.
        return "".join(path)