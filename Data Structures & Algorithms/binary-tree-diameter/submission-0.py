# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def contain(root):
            if root is None:
                return 0
            
            if root.left is None and root.right is None:
                return 0
            
            return 1 + max(contain(root.left), contain(root.right))
        
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 0
        
        max_path = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        if root.left is None:
            max_path = max(max_path, 1 + contain(root.right))
        
        if root.right is None:
            max_path = max(max_path, 1 + contain(root.left))
        
        if root.left and root.right:
            max_path = max(max_path, 2 + contain(root.left) + contain(root.right))
        
        return max_path