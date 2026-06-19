class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_list = sorted(intervals, key=lambda x: x[0])
        res = []
        if len(sorted_list) == 1:
            return sorted_list
        min_val, max_val = sorted_list[0][0], sorted_list[0][1]
        new_list = [min_val, max_val]
        for i in range(1, len(sorted_list)):
            if max_val >= sorted_list[i][0]:
                min_val = min(min_val, sorted_list[i][0])
                max_val = max(max_val, sorted_list[i][1])
                new_list = [min_val, max_val]
            else:
                res.append(new_list)
                min_val, max_val = sorted_list[i][0], sorted_list[i][1]
                new_list = [min_val, max_val]
            
        res.append(new_list)
        return res