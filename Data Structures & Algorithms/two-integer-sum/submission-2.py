class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_list = []
        for num1 in range(len(nums)):
            for num2 in range(len(nums)):
                if nums[num1] + nums[num2] == target:
                    final_list.append(num1)
                    final_list.append(num2)
                else:
                    continue
        