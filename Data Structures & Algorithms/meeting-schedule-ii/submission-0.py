"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        total = list()
        for interval in intervals:
            total.append([interval.start, interval.end])
        
        max_num = 0

        for i in range(len(total)):
            count = 0
            for j in range(len(total)):
                if total[j][0] <= total[i][0] < total[j][1]:
                    count += 1
            
            if count > max_num:
                max_num = count
            
            count = 0

            for j in range(len(total)):
                if total[j][0] < total[i][1] <= total[j][0]:
                    count += 1
            
            if count > max_num:
                max_num = count
        
        return max_num