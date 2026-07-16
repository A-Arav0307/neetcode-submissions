from collections import defaultdict
class Solution:
    
    def checkValidString(self, s: str) -> bool:

        stars = []
        stack = []

        for i, char in enumerate(s): 
            if char == '(':
                stack.append([i, char]) 
            elif char == '*':
                stars.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                elif not stack and stars: 
                    stars.pop()
                else: 
                    return False

        print(stack)
        print(stars)
        if not stack:
            return True 
        if len(stars) < len(stack):
            return False
        for i in range(len(stack)-1, -1, -1):
            if stars[-1] < stack[i][0]:
                return False
            stars.pop()
            stack.pop()

        return True if not stack else False

         


        