class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_list = []
        
        for n in range(len(nums)-2):
            if n > 0 and nums[n] == nums[n-1]:
                continue
            l = n
            r = len(nums) - 1

            while l < r:
                target = nums[n] + nums[l] + nums[r]
                if target < 0:
                    l += 1 
                elif target > 0 and r >= 0:
                    r -= 1
                else:
                    #target = 0
                    final_list.append([nums[n], nums[l], nums[r]])
                    l += 1 
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

        return final_list
