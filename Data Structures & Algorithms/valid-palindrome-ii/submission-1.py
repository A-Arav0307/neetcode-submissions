class Solution:
    def validPalindrome(self, s: str) -> bool:
        deletions = 0 
        right = False
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]: 
                l += 1 
                r -= 1
            if s[l] != s[r] and not right:
                if deletions != 0:
                    right = True 
                    deletions = 0
                    r += 1
                    l -= 1
                else:
                    r -= 1
                    deletions += 1

            if s[l] != s[r] and right:
                if deletions != 0:
                    return False 
                else:
                    l += 1
                    deletions += 1
        return True 