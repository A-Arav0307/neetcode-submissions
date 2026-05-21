class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        house_left = nums[0:n-1]
        house_right = nums[1:n]

        def rob_homes(homes):
            n = len(homes)

            if n == 1:
                return homes[0]
            if n == 2:
                return max(homes[0], homes[1])

            value_list = [0] * len(nums)
            value_list[0] = homes[0]
            value_list[1] = max(homes[0], homes[1])
            for i in range(2, n):
                value_list[i] = max(value_list[i-1], value_list[i-2] + homes[i])
            return value_list[n-1]

        dp_left = rob_homes(house_left)
        dp_right = rob_homes(house_right)

        return max(dp_left, dp_right)
