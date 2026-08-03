class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals) == 1:
            return intervals
        min_val, max_val = intervals[0][0], intervals[0][1]
        new_list = [min_val, max_val]
        for i in range(1, len(intervals)):
            if max_val >= intervals[i][0]:
                min_val = min(min_val, intervals[i][0])
                max_val = max(max_val, intervals[i][1])
                new_list = [min_val, max_val]
            else:
                res.append(new_list)
                return res + intervals[i:]
            
        res.append(new_list)
        return res