# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def add(node):
            if not node:
                return
            add(node.left)
            arr.append(node.val)
            add(node.right)
        add(root)
        return arr[k-1]
