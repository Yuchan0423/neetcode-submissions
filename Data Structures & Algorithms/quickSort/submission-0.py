# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def quickSort_huge(arr,s,e):
            if e <= s:
                return arr
            pivot = arr[e].key
            left = s
            for i in range(s,e):
                if arr[i].key < pivot:
                    arr[i] , arr[left] = arr[left] , arr[i]
                    left += 1
            arr[e] , arr[left] = arr[left] , arr[e]
            quickSort_huge(arr,s,left-1)
            quickSort_huge(arr,left+1,e)
        quickSort_huge(pairs, 0, len(pairs)-1)
        return pairs