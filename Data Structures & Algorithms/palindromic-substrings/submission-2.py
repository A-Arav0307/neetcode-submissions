class Solution:
    def countSubstrings(self, s: str) -> int:
        # Odd length substrings
        odd_substrings = 0
        for i in range(len(s)):
            j = i
            while i >= 0 and j <= len(s) - 1:
                if s[i] == s[j]:
                    odd_substrings += 1
                    i -= 1
                    j += 1 
                else:
                    break
                

        even_substrings = 0
        for i in range(len(s)-1):
            j = i + 1
            while i >= 0 and j <= len(s) - 1:
                if s[i] == s[j]:
                    even_substrings += 1
                    i -= 1
                    j += 1
                else:
                    break
                
        total_substrings = odd_substrings + even_substrings
        return total_substrings