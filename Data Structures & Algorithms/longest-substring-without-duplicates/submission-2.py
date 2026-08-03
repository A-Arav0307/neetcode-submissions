class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #had to watch video to solve this
        characters = set()
        length = 1
        l = 0
        for r in range(len(s)):
            while s[r] in characters:
                characters.remove(s[l])
                l += 1

            characters.add(s[r])
            length = max(length, r - l + 1)

        return length