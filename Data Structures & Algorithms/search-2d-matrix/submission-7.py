class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_small, r_large = 0, len(matrix)-1
        #find row where target could be
        while r_small < r_large:
            mid = (r_small + r_large) // 2
            if target <= max(matrix[mid]) and target >= min(matrix[mid]): 
                r_small = mid
                break 
            
            elif target >= max(matrix[mid]):
                r_small = mid + 1

            else:
                r_large = mid

        print(r_small)
        final_row = r_small
        #perform basic binary search
        nums = matrix[final_row]

        l, r = 0, len(nums)-1 
        if len(nums) == 1:
            if target == nums[0]:
                return True
            return False
            
        while l < r:
            if nums[l] == target or nums[r] == target:
                return True 
            mid = (l+r) // 2 
            if nums[mid] == target:
                return True 
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return False
        