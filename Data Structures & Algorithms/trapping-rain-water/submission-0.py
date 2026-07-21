class Solution:
    def trap(self, height: List[int]) -> int:
        left_trap = [0 for _ in range(len(height) + 1)]

        for i in range(len(height) - 1, -1, -1):
            left_trap[i] = max(height[i], left_trap[i + 1])
        
        curr = 0
        water = 0
        for i in range(len(height) - 1):
            if height[i] >= water:
                water = height[i]
                if water > left_trap[i + 1]:
                    water = left_trap[i + 1]
            else:
                curr = curr + water - height[i]
        
        return curr
            
                
            