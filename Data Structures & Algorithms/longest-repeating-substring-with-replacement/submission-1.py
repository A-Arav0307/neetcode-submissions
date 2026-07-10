from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # {'X': 2, 'Y': 2}
        l = 0
        count = defaultdict(int)
        length = float('-inf')
        
        for r in range(len(s)):
            count[s[r]] += 1
            new_len = r-l+1
            if new_len - max(count.values()) <= k:
                length = max(length, new_len)
            else:
                while r-l+1 - max(count.values()) > k:
                    count[s[l]] -= 1
                    l += 1

        return length 

