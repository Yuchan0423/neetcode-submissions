class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = set()
        visited.add(-1)
        def dfs(pos):
            if pos >= len(nums) - 1:
                return True

            if pos <= -1:
                return False
            
            while pos not in visited:
                visited.add(pos)
                if dfs(pos + nums[pos]):
                    return True
                pos -= 1
            return False
        
        return dfs(0)


        