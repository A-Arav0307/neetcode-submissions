import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)

        popped = []
        for _ in range(k):
            popped.append(-heapq.heappop(heap))

        return popped[-1]   
