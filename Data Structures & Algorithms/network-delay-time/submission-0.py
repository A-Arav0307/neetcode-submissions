import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = float('-inf')
        visited = set()
        adj = {i:[] for i in range(1, n+1)}
        for start, end, weight in times:
            adj[start].append((end, weight))
        heap = [ [0,k] ]
        heapq.heapify(heap)
        while heap: 
            cost, node = heapq.heappop(heap) 
            if node in visited: 
                continue
            visited.add(node) 
            time = max(time, cost) 
            for neighbor, new_cost in adj[node]:
                heapq.heappush(heap, [cost + new_cost, neighbor])
                

        return time if len(visited) == n else -1 
        