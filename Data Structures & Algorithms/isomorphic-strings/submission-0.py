class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        if len(s) != len(t):
            return False

        l = 0

        while l < len(s):
            if s[l] not in map:
                if t[l] in map.values():
                    return False
                map[s[l]] = t[l]
                
            elif s[l] in map:
                value = map[s[l]]
                if value != t[l]:
                    return False

            l += 1
               
            

        return True 