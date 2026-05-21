class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = nums[l]

        while l < r: 
            middle = (l + r) // 2
            if nums[middle] > nums[r]:
                l = middle+1
                minimum = nums[r]
            if nums[middle] < nums[r]:
                r = middle
                minimum = nums[middle]

        return minimum
        