# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        if root.left is not None:
            curr = root.left
            while curr.right:
                curr = curr.right
            if curr.val >= root.val:
                return False
        
        if root.right is not None:
            curr = root.right
            while curr.left:
                curr = curr.left
            if root.val >= curr.val:
                return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)