class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        left = 0
        s1_dict = {}
        for c in s1:
            s1_dict[c] = 1 + s1_dict.get(c, 0)
            
        s2_dict = {}
        for right in range(len(s2)):
            if s2[right] not in s1_dict:
                s2_dict.clear()
                left = right + 1
                continue
            
            s2_dict[s2[right]] = 1 + s2_dict.get(s2[right], 0)
            
            while s2_dict[s2[right]] > s1_dict[s2[right]]:
                s2_dict[s2[left]] -= 1
                left += 1
  
            if (right - left == length - 1) \
    and (s2_dict[s2[right]] == s1_dict[s2[right]]):
                return True
        
        return False