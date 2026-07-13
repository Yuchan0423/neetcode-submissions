class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_ones = 0
        one_direction = 0
        product = 1
        product_list = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                num_ones += 1
                one_direction = i
            else:
                product *= nums[i]
        
        if num_ones >= 2:
            return product_list
        
        if num_ones == 1:
            product_list[one_direction] = product
            return product_list
        
        for i in range(len(nums)):
            product_list[i] = product // nums[i]

        return product_list
        

        