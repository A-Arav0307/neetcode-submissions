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
                    r = breaking_r
                    l = breaking_l
                else:
                    breaking_r = r
                    breaking_l = l
                    r -= 1
                    deletions += 1

            if s[l] != s[r] and right:
                if deletions != 0:
                    return False 
                else:
                    l += 1
                    deletions += 1
        return True 