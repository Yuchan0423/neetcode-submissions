class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right_max = [0 for _ in range(len(heights))]
        left_max = [0 for _ in range(len(heights))]    

        right_stack = []
        for i in range(len(heights)):
            while right_stack and heights[right_stack[-1]] > heights[i]:
                right_max[right_stack.pop()] = i - 1
            right_stack.append(i)
        for num in right_stack:
            right_max[num] = len(heights) - 1
        
        left_stack = []
        for i in range(len(heights) - 1, -1, -1):
            while left_stack and heights[left_stack[-1]] > heights[i]:
                left_max[left_stack.pop()] = i + 1
            left_stack.append(i)
        
        for num in left_stack:
            left_max[num] = 0

        max_block = 0
        for i in range(len(heights)):
            max_block = max(max_block, heights[i] * (right_max[i] - left_max[i] + 1))
        
        return max_block