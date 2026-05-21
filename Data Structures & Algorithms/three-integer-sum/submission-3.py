class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_list = []

        for n in range(len(nums) - 2):
            if n > 0 and nums[n] == nums[n - 1]:
                continue

            l = n + 1
            r = len(nums) - 1

            while l < r:
                total = nums[n] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    final_list.append([nums[n], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return final_list