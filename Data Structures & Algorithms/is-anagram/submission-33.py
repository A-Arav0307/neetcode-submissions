class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False 

        s_characters = {}
        t_characters = {}

        for s_char in s: 
            if s_char not in s_characters: 
                s_characters[s_char] = 1
            s_characters[s_char] += 1 

        for t_char in t: 
            if t_char not in t_characters:
                t_characters[t_char] = 1
            t_characters[t_char] += 1

        for key in s_characters.keys(): 
            if key not in t_characters: 
                return False 
            if s_characters[key] != t_characters[key]: 
                return False 
            

        return True 

       