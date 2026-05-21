class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False
            
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
    
        for key in dict1.keys(): 
            if key not in dict2 or dict1[key] != dict2[key]: 
                return False
        return True
    
