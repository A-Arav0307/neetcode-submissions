class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #had to watch video to solve this
        if not s:
            return 0
        longest = float('-inf') 
        l, r = 0, 0
        visited = set() 
        while r < len(s):
            if s[r] not in visited:
                visited.add(s[r])
                r += 1
                longest = max(longest, r-l)
            else:
                while s[r] in visited: 
                    if s[l] == s[r]:
                        visited.remove(s[l])
                    else:
                        l += 1
                l += 1
        

        return longest