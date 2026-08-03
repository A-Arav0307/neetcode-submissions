class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        list_lengths = []
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            else:
                length = 0
                current = num
                while current in nums_set:
                    length += 1
                    current += 1
                list_lengths.append(length)
                length = 1

        return max(list_lengths)
