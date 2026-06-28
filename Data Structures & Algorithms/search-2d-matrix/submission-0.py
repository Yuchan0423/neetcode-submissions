class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix) - 1
        while L < R:
            mid = (L+R) // 2
            if matrix[mid][-1] < target:
                L = mid + 1
            elif matrix[mid][-1] > target:
                R = mid 
            else:
                return True
        arr = matrix[L]
        L = 0
        R = len(arr) - 1
        while L <= R:
            mid = (L+R) // 2
            if arr[mid] < target:
                L = mid + 1
            elif arr[mid] > target:
                R = mid - 1
            else:
                return True
        return False
        
