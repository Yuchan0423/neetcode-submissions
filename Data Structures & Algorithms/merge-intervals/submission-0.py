class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        ans = []
        start, end = 0, 0
        max_num = intervals[0][1]
        while end < len(intervals):
            if max_num < intervals[end][0]:
                ans.append([intervals[start][0], max_num])
                start = end
                max_num = intervals[end][1]
            else:
                max_num = max(max_num, intervals[end][1])
            end += 1
        ans.append([intervals[start][0], max_num])

        return ans