class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        res = []
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            frequency[num] += 1

        for num in frequency:
            buckets[frequency[num]-1].append(num)

            
        #[[], [1], [2], [3, 4], [], [], []]

        for i in range(len(buckets)-1, -1, -1):
            if not buckets[i]:
                continue
            for num in buckets[i]:
                if k > 0:
                    res.append(num)
                    k -= 1
            
        return res
            