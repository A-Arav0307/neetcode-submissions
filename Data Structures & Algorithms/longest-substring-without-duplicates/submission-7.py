from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0
        length = float('-inf') 
        l = 0
        freq = defaultdict(int) 
        for r in range(len(s)): 
            freq[s[r]] += 1
            if freq[s[r]] > 1:
                while freq[s[r]] > 1: 
                    freq[s[l]] -= 1
                    l += 1

            length = max(length, r-l+1)

        return length
