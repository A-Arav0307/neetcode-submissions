class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')' : '(', '}': '{', ']': '['}

        if len(s) == 1 or s[0] in check: 
            return False 

        for character in s: 
            if character not in check: 
                stack.append(character)
            if character in check:
                if stack[-1] != check[character]: 
                    return False
                else:
                    stack.pop(-1)

        return True 