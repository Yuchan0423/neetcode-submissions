class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def quicksort(arr,s,e):
            if e <= s:
                return arr
            pivot = arr[e][0] ** 2 + arr[e][1] ** 2
            left = s
            for i in range(s,e):
                if arr[i][0] ** 2 + arr[i][1] ** 2 < pivot:
                    arr[left] , arr[i] = arr[i] , arr[left]
                    left += 1
            arr[e] , arr[left] = arr[left] , arr[e]
            quicksort(arr,s,left-1)
            quicksort(arr,left+1,e)
        quicksort(points,0,len(points)-1)
        return points[:k]