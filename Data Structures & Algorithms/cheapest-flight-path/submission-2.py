class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = [float('inf') for i in range(n)]
        distances[src] = 0 

        for i in range(k+1):
            temp_distances = distances[:]
            for start, end, cost in flights:
                if distances[start] != float('inf') and distances[start] + cost < temp_distances[end]:
                    temp_distances[end] = distances[start] + cost 

            distances = temp_distances
        return distances[dst] if distances[dst] != float('inf') else -1