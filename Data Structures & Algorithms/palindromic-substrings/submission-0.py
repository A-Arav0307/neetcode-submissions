class Solution:
    def countSubstrings(self, s: str) -> int:
        num_palindromes = 0
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    num_palindromes += 1 
        return num_palindromes