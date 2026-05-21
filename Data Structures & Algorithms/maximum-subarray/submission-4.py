class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)

    def maxSubArrayHelper(self, nums, l, r):
        if l == r:
            return nums[l]

        middle = (l + r) // 2

        leftTotal = self.maxSubArrayHelper(nums, l, middle)
        rightTotal = self.maxSubArrayHelper(nums, middle + 1, r)

        left = float('-inf')
        curr = 0
        for i in range(middle, l - 1, -1): 
            curr += nums[i]
            left = max(left, curr)

        right = float('-inf')
        curr = 0
        for i in range(middle + 1, r + 1): 
            curr += nums[i]
            right = max(right, curr)

        mergeTotal = left + right
        return max(mergeTotal, left, right)
        