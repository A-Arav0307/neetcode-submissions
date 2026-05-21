class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""
        
        longest = ""
        
        #Odd length substring
        for i in range(len(s)):
            j = i
            while i >= 0 and j <= len(s)-1 and s[i] == s[j]:
                if (j-i + 1) > len(longest):
                    longest = s[i:j+1]
                i -= 1
                j += 1

        #even substring
        for i in range(len(s)-1):
            j = i+1
            while i >= 0 and j <= len(s)-1 and s[i] == s[j]:
                if (j-i + 1) > len(longest):
                    longest = s[i:j+1]
                i -= 1
                j += 1

        return longest