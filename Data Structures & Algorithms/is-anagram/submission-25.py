class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for letter in s: 
            if letter not in dict1: 
                dict1[letter] = 1
            dict1[letter] += 1

        for letter in t:
            if letter not in dict2:
                dict2[letter] = 1
            dict2[letter] += 1
    
        for key in s_dict: 
            if key not in t_dict or s_dict[key] != t_dict[key]: 
                return False
            return True
    
