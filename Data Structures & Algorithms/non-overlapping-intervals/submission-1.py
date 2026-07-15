class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda li : li[0])
        length = len(intervals)
        max_count = [1] * length
        max_count.append(0)

        max_till = [1] * length
        max_till.append(0)

        for i in range(length - 2, -1, -1):
            L = i + 1 
            R = length
            while L < R :
                mid = (L + R) // 2
                if intervals[mid][0] >= intervals[i][1]:
                    R = mid
                else:
                    L = mid + 1
            max_count[i] = max_till[L] + 1
            max_till[i] = max(max_till[i + 1], max_count[i])
        
        return length - max(max_count)