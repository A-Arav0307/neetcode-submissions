class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        length = float('-inf')
        for num in nums:
            num_set.add(num)
        
        list_lengths = []
        for num in nums:
            new_length = 0
            if num-1 in num_set:
                continue
            else:
                while num in num_set:
                    new_length += 1
                    num += 1
                length = max(length, new_length)
        
        return length