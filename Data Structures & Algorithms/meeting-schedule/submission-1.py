"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        dic = {}

        for interval in intervals:
            if interval.start in dic:
                return False
            dic[interval.start] = interval.end

        start_points = sorted(list(dic.keys()))

        for i in range(len(start_points) - 1):
            if dic[start_points[i]] > start_points[i + 1]:
                return False
        
        return True