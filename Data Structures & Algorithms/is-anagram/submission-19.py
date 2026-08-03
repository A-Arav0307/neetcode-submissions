class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        s_dict = {}
        t_dict = {}

        for letter in s: 
            if letter not in s_dict: 
                s_dict[letter] = 0
            s_dict[letter] += 1

        for letter in t: 
            if letter not in t_dict: 
                t_dict[letter] = 1
            t_dict[letter] += 1

        for key in s_dict: 
            if key not in t_dict or s_dict[key] != t_dict[key]: 
                return False
        return True