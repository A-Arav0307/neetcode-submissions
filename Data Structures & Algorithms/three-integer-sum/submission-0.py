class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = 0
        r = len(nums) - 1
        final_list = []
        while l < r:
            target = 0 - (nums[l]+nums[r])
            for k in range(l+1, r):
                if nums[k] == target:
                    triplet = [nums[l], nums[k], nums[r]]
                    if triplet not in final_list: 
                        final_list.append(triplet)
                        break

            if target > 0:
                l += 1 
            elif target < 0: 
                r -= 1
            else:
                l+=1
                r -= 1

        return final_list
                