class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        length = 1
        hash_set = set()
        i, j = 0, 0

        while i < len(s):
            if s[i] not in hash_set:
                hash_set.add(s[i])
                j += 1
                length = max(length, j)
                i += 1
            else:
                hash_set = set()
                j = 0

        return length