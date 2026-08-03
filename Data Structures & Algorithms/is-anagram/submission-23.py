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
    
        counter = 0
        for key, value in dict1.items(): 
            if key not in dict2:
                return False
            if dict1[key] == dict2[key]: 
                counter += 1
            
        if counter == len(s): 
            return True
        else: 
            return False
    
