# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        track = dict()

        def maxroot(node):
            if node is None:
                return 0

            if node in track:
                return track[node]
            
            track[node] = node.val + max(0, maxroot(node.left), maxroot(node.right))

            return track[node]
        
        maxroot(root)

        real_track = dict()

        def realmaxroot(node):
            if node is None:
                return 0

            if node in real_track:
                return real_track[node]
            
            real_track[node] = node.val + max(0, maxroot(node.left)) + max(0, maxroot(node.right))

            realmaxroot(node.left)
            realmaxroot(node.right)
        
        realmaxroot(root)

        return max(real_track.values()) if real_track is not None else 0
            
        
