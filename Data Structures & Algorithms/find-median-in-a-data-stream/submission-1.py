import heapq
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []



    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            value = heapq.heappop(self.small)
            heapq.heappush(self.large, -value)
        
        if len(self.small) - len(self.large) > 1:
            value = heapq.heappop(self.small)
            heapq.heappush(self.large, -value) 
    

        if len(self.large) - len(self.small) > 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            if self.small and self.large:
                val1 = -self.small[0]
                val2 = self.large[0]
                return (val1 + val2) / 2
        