class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        times = 0
        #change min, max to max and min of both if overlap otherwise else
        # min, max is just the values of that index
        [[1, 2], [2, 4], [1, 4]]
        if len(intervals) == 1: 
            return 0
        min_val, max_val = intervals[-1][0], intervals[-1][1]
        sorted_list = sorted(intervals, key=lambda x: x[1])
        for i in range(len(intervals)-2, -1, -1):
            if min_val < intervals[i][1]:
                times += 1
                min_val = max(min_val, intervals[i][0])
                max_val = max(max_val, intervals[i][1]) 
                intervals[i] = [min_val, max_val] 

        
        return times 