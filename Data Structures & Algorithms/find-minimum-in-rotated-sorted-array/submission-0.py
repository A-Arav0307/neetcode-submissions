class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = nums[l]

        while l < r: 
            middle = (l + r) // 2
            if nums[l] < nums[r]:
                r = middle
                minimum = nums[l]
            else:
                l = middle
                minimum = nums[r]
        return minimum
        