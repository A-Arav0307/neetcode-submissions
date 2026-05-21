class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        length = 0
        for num in nums:
            num_set.add(num)
        
        list_lengths = []
        for num in nums:
            if num-1 in num_set:
                continue
            else:
                while num in num_set:
                    length += 1
                    num += 1
                list_lengths.append(length)
                length = 0
        
        return max(list_lengths) if list_lengths else 0