import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        heap = []
        if a > 0:
            heap.append((-a, "a"))
        if b > 0: 
            heap.append((-b, "b"))
        if c > 0:
            heap.append((-c, "c"))
        heapq.heapify(heap)
        while heap:
            value, char = heapq.heappop(heap) 
            if len(result) > 1:
                if result[-1] == char and result[-2] == char: 
                    if not heap: 
                        break 
                    next_count, next_char = heapq.heappop(heap)
                    result.append(next_char)

                    if next_count + 1 < 0: 
                        heapq.heappush(heap, (next_count+1, next_char))

            result.append(char)
            if value + 1 < 0:
                heapq.heappush(heap, (value+1, char))

        return "".join(result) 
                