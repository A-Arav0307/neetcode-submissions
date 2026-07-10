from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        def check(w1, w2):
            for char in w1:
                if w1[char] != w2[char]:
                    return False
            return True

        word1 = defaultdict(int)
        word2 = defaultdict(int) 

        for char in s1:
            word1[char] += 1

        l = 0 
        for r in range(len(s2)):
            word2[s2[r]] += 1
            if r - l + 1 > len(s1):
                word2[s2[l]] -= 1
                l += 1 
            
            if r - l + 1 == len(s1):
                if check(word1, word2):
                    return True

        return False
                

