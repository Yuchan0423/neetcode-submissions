class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return 0

        max_vol = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            max_vol = max(max_vol, (R - L) * min(heights[L], heights[R]))

            if heights[L] < heights[R]:
                curr = heights[L]
                while L < R and heights[L] <= curr:
                    L += 1
            else:
                curr = heights[R]
                while L < R and heights[R] <= curr:
                    R -= 1
        
        return max_vol