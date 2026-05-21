class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = []
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        for i in range(len(nums)+1):
            frequency.append([])
        
        for n, c in count.items():
            frequency[c].append(n)
        res = []
        for i in range(len(frequency)-1, 0, -1):
            if not frequency[i]:
                continue
            else:
                for value in frequency[i]:
                    res.append(value)
            if len(res) == k:
                return res