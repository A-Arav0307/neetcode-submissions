class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: 
            return True 
        
        if (s[0] == '(' and s[-1] != ')') or (s[0] == '{' and s[-1] != '}') or (s[0] == '[' and s[-1] != ']'): 
            return False 

        else: 
            return self.isValid(s[1: len(s)-1])