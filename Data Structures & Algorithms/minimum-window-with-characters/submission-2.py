from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        strings = []
        if len(s) < len(t):
            return ""
        check = defaultdict(int)
        word = defaultdict(int) 
        for char in t:
            check[char] += 1

        def valid(w1, w2): # w1 always being check!
            for char in w1:
                if char not in w2 or w1[char] != w2[char]:
                    return False
            return True
        l = 0
        for r in range(len(s)):
            word[s[r]] += 1
            if not valid(check, word):
                continue
            else:
                while valid(check, word):
                    strings.append(  (s[l:r+1], len(s[l:r+1]))  )
                    word[s[l]] -= 1 
                    l += 1
        if not strings:
            return ''
        print(strings)
        min_tuple = min(strings, key=lambda x: x[1])
        min_string, num = min_tuple
        return min_string