class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')' : '(', '}': '{', ']': '['}

        for character in s: 
            if character in check: 
                if len(stack) > 0 and stack[-1] == check[character]: 
                    stack.pop(-1) 
                else: 
                    return False
            
            else: 
                stack.append(character)

        return True