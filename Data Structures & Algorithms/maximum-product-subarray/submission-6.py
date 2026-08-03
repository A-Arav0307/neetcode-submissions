class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        value_list = [1] * n
        value_list[0] = nums[0]
        product = nums[0]

        for i in range(1, n):
            product *= nums[i]
            if product >= value_list[i]:
                value_list[i] = product
            else:
                value_list[i] = max(nums[i], value_list[i-1])

        return max(value_list)