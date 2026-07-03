import heapq 
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        final_cost = 0
        def cost(i, j): 
            x1, y1 = points[i]
            x2, y2 = points[j]
            val = abs(x1-x2) + abs(y1-y2) 
            return val 

        visit = set([0])
        n = len(points)
        heap = []
        heapq.heapify(heap)
        for j in range(1, n): 
            heapq.heappush(heap, [cost(0, j), j])

        while len(visit) < n:
            new_cost, index = heapq.heappop(heap)
            if index in visit:
                continue
            visit.add(index) 
            final_cost += new_cost
            
            for nei in range(n):
                if nei not in visit:
                    heapq.heappush(heap, [cost(index, nei), nei])


        return final_cost