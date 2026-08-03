class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] == target:
            return l

        while l < r: 
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            middle = (l+r) // 2
            if nums[middle] == target:
                return middle
            
            if nums[middle] > nums[r] and target < nums[middle]:
                l = middle + 1
            if nums[middle] > nums[r] and target > nums[middle]:
                l = middle + 1

            if nums[middle] < nums[r] and target < nums[middle]:
                r = middle - 1
            if nums[middle] < nums[r] and target > nums[middle]:
                l = middle + 1


        return -1