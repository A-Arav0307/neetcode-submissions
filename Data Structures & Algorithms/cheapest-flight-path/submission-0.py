class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for start, end, cost in flights:
            adj[start].append((end, cost)) 
        heap = [ [0, src, 0] ]
        heapq.heapify(heap) 

        while heap:
            cost, location, stops = heapq.heappop(heap)
            if stops > k + 1: 
                continue
            if location == dst:
                return cost
            for neighbor in adj[location]:
                new_location, new_cost = neighbor
                heapq.heappush(heap, [cost+new_cost, new_location, stops+1])

        return -1