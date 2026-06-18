import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        frequency = {}
        for letter in s:
            if letter not in frequency:
                frequency[letter] = 0
            frequency[letter] += 1

        heap = []
        for key, value in frequency.items(): 
            heap.append((-value, key))
        heapq.heapify(heap) 

        while heap: 
            value, char = heapq.heappop(heap)
            if len(res) > 0 and char == res[-1]:
                if not heap:
                    break
                next_value, next_char = heapq.heappop(heap) 
                res.append(next_char)
                if next_value + 1 < 0:
                    heapq.heappush(heap, (next_value+1, next_char))
                    

            res.append(char)
            if value + 1 < 0:
                heapq.heappush(heap, (value+1, char))

        if len(res) == len(s):
            return "".join(res)
        else:
            return ""