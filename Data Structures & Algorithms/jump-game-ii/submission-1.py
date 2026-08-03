class Solution:
    def jump(self, nums: List[int]) -> int:
        values = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                continue
            new_index = i + nums[i]
            values[i] = 1 + min(values[i+1 : new_index+1])

        return values[0] 