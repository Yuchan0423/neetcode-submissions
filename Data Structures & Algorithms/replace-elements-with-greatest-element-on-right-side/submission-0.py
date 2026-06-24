class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cnt = -1
        i = len(arr)-1

        while i >= 0:
            t = arr[i]
            arr[i] = cnt
            cnt = max(cnt,t)
            i = i-1

        return arr