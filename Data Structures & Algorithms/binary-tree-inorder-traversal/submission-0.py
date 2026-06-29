# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        arr = self.inorderTraversal(root.left)
        arr.append(root.val)
        arr_right = self.inorderTraversal(root.right)
        while arr_right:
            arr.append(arr_right.pop(0))
        return arr
        