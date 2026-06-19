class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        times = 0
        #change min, max to max and min of both if overlap otherwise else
        # min, max is just the values of that index
        [[1, 2], [1, 3], [2,3], [3, 4]]
        if len(intervals) == 1: 
            return 0
        sorted_list = sorted(intervals, key=lambda x: x[1])
        min_val, max_val = sorted_list[-1][0], sorted_list[-1][1]
        for i in range(len(sorted_list)-2, -1, -1):
            if min_val < sorted_list[i][1]:
                times += 1
                min_val = max(min_val, sorted_list[i][0])
                max_val = max(max_val, sorted_list[i][1]) 
                sorted_list[i] = [min_val, max_val] 
            else:
                min_val, max_val = sorted_list[i][0], sorted_list[i][1]

        
        return times 