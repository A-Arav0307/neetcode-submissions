import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = {}
        for task in tasks:
            if task not in frequency:
                frequency[task] = 0
            frequency[task] += 1

        q = deque()
        freq = list(frequency.values())
        heap = [-s for s in freq]
        heapq.heapify(heap)
        time = 0
        

        while heap or q: 
            time += 1

            if heap:
                count = 1 + heapq.heappop(heap) 
                if count < 0:
                    q.append([count, time + n])

            if q: 
                if q[0][1] == time:
                    new_val, new_time = q.popleft()
                    heapq.heappush(heap, new_val) 

        return time 
            
