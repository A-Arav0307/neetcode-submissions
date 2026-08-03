class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')' : '(', '}': '{', ']': '['}

        for character in s: 
            if character not in check: 
                stack.append(character)
            
            if character in check: 
                if len(stack) > 0 and stack[-1] == check[character]: 
                    stack.pop(-1) 
                else: 
                    return False

        return True