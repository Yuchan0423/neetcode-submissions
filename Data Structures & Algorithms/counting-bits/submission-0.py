class Solution:
    def countBits(self, n: int) -> List[int]:
        
        arr = [0]
        for i in range(1, n + 1):
            val = arr[i >> 1] 
            if i & 1 == 1:
                arr.append(val + 1)
            else:
                arr.append(val)
        
        return arr