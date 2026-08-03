class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        areas = []
        while l < r:
            area = (r-l) * min(heights[r], heights[l])
            areas.append(area)

            if heights[l] > heights[r] and r >= 0:
                r -= 1

            if heights[l] < heights[r] and l <= len(heights)-1:
                l += 1
            
            else:
                l += 1
                r -= 1

        return max(areas)