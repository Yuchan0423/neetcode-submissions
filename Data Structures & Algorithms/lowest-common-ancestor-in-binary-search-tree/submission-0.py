# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def inside(root, node):

            if root is None:
                return False
                
            if root.val == node.val:
                return True
            
            return inside(root.left, node) or inside(root.right, node)
        
        if inside(root.left, p) and inside(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        
        if inside(root.right, p) and inside(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
        