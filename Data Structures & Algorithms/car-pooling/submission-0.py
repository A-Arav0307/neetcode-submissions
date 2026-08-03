import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        intervals = []
        for trip in trips:
            interval = []
            if trip[0] > capacity:
                return False
            interval.append(trip[1])
            interval.append(trip[2])
            intervals.append(interval)
        
        #check if intervals merge
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        max_val = sorted_intervals[0][1]
        for i in range(1, len(sorted_intervals)):
            if max_val > sorted_intervals[i][0]:
                return False
            max_val = sorted_intervals[i][1]

        return True 