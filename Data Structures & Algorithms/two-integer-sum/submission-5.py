class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for num1 in range(len(nums)):
            for num2 in range(num1+1,len(nums)):
                if nums[num1] + nums[num2] == target:
                    final_list = [num1, num2]
                    final_list.sort()
        
        return final_list
        