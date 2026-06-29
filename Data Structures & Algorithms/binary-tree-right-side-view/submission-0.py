# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        arr = []
        quere = [root]
        while len(quere) > 0:
            curr = quere
            quere , val = [] , []
            while len(curr) > 0:
                node = curr.pop(0)
                if node.left:
                    quere.append(node.left)
                if node.right:
                    quere.append(node.right)
                val.append(node.val)
            arr.append(val[-1])
        return arr
        