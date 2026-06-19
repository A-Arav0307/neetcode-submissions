class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sorted_list = sorted(intervals, key=lambda x: x[0])
        res = []
        for i in range(len(sorted_list)):
            if newInterval[1] < sorted_list[i][0]:
                res.append(newInterval)
                return res + sorted_list[i:]
            elif newInterval[0] > sorted_list[i][1]:
                res.append(sorted_list[i])
            else:
                newInterval = [min(newInterval[0], sorted_list[i][0]), max(newInterval[1], sorted_list[i][1])]

        res.append(newInterval)
        return res 
            