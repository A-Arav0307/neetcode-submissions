"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_list = sorted(intervals, key=lambda x: x.start)
        tuple_list = [(interval.start, interval.end) for interval in sorted_list]
        if len(tuple_list) == 1: 
            return True
        max_val = tuple_list[0][1]
        for i in range(1, len(tuple_list)):
            if max_val > tuple_list[i][0]:
                return False 
            max_val = tuple_list[i][1]
        
        return True