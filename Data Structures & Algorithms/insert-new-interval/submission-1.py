class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = list()
        N = len(intervals)
        left , right = 0 , N - 1
        while left < N and intervals[left][1] < newInterval[0]:
            left = left + 1
        
        while right >= 0 and intervals[right][0] > newInterval[1]:
            right = right - 1
        
        for i in range(left):
            output.append(intervals[i])
        
        interval_left = min(newInterval[0], intervals[left][0]) if left < N else newInterval[0]

        interval_right = max(newInterval[1], intervals[right][1]) if right >= 0 else newInterval[1]

        output.append([interval_left, interval_right])

        for i in range(right + 1, N):
            output.append(intervals[i])

        return output

        

            
        
        
        
        

        
        
        