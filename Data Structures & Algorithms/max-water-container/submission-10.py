class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        area = float('-inf') 
        while l < r: 
            new_area = (r-l) * min(heights[l], heights[r]) 
            area = max(area, new_area)
            if heights[l] > heights[r]: 
                r -= 1
            elif heights[r] > heights[l]: 
                l += 1
            else:
                l += 1

        return area 