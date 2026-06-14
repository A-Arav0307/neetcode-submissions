class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        
        s_dict = {}
        for letter in s: 
            if letter in s_dict: 
                s_dict[letter] += 1
            if letter not in s_dict: 
                s_dict[letter] = 1

        t_dict = {}
        for letter in t: 
            if letter in t_dict: 
                t_dict[letter] += 1
            if letter not in t_dict: 
                t_dict[letter] = 1

        for letter in s: 
            if letter not in t_dict:
                return False
            elif s_dict[letter] != t_dict[letter]: 
                return False 

        return True 