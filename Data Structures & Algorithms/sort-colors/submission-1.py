class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            frequency[num] += 1


        index = 0
        for value in range(0, 3):
            if value not in frequency:
                continue 
            for i in range(index, index + frequency[value]):
                nums[i] = value 

            index += frequency[value]