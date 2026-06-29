# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.right is None:
                root = root.left
            elif root.left is None:
                root = root.right
            else:
                curr = root.right
                if curr.left is None:
                    root.val = curr.val
                    root.right = self.deleteNode(root.right,curr.val)
                else:
                    while curr.left.left:
                        curr = curr.left
                    val = curr.left.val
                    root.val = val
                    root.right = self.deleteNode(root.right, val)
        return root
            