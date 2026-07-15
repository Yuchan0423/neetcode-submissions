# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        in_p = deque()
        in_q = deque()

        p_root = root
        while p_root.val != p.val:
            in_p.append(p_root)
            if p_root.val < p.val:
                p_root = p_root.right
            else:
                p_root = p_root.left
        
        in_p.append(p_root)
        
        q_root = root
        while q_root.val != q.val:
            in_q.append(q_root)
            if q_root.val < q.val:
                q_root = q_root.right
            else:
                q_root = q_root.left

        in_q.append(q_root)
        
        ans = root
        while in_p and in_q:
            pop_p = in_p.popleft()
            pop_q = in_q.popleft()

            if pop_p == pop_q:
                ans = pop_p
            
            else:
                return ans
        
        return ans