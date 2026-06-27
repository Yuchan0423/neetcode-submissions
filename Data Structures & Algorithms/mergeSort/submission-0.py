# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def mergeS(arr,s,e):
            if e <= s:
                return arr

            m = (s+e) // 2

            mergeS(arr,s,m)

            mergeS(arr,m+1,e)

            merge(arr,s,m,e)

        def merge(arr,s,m,e):
            L = arr[s:m+1]
            R = arr[m+1:e+1]
            i = 0
            j = 0
            k = s
            while i < len(L) and j < len(R):
                if L[i].key > R[j].key:
                    arr[k] = R[j]
                    j += 1
                else:
                    arr[k] = L[i]
                    i += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        mergeS(pairs,0,len(pairs)-1)
        return pairs
