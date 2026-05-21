class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        length = 1
        for num in nums:
            num_set.add(num)
        
        list_lengths = []
        for num in nums:
            while num + 1 in num_set:
                length += 1
                num += 1
            list_lengths.append(length)
            length = 1
        
        return max(list_lengths) if nums else 0