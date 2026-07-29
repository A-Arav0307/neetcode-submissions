class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        area = 0

        for r in range(len(heights)):
            while stack and heights[r] < heights[stack[-1]]: 
                popped_index = stack.pop()
                height = heights[popped_index] 
                
                left = stack[-1] if stack else -1 
                width = r - left - 1

                area = max(area, height * width)

            stack.append(r) 

        return area