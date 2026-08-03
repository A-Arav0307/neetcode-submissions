class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        final_s_values = []
        final_t_values = []
        
        for letter in range(len(s)):
            s_letter = s[letter]
            t_letter = t[letter]
            if s_letter not in s_dict:
                s_dict[letter] = 1
            s_dict[letter] += 1

            if t_letter not in t_dict:
                t_dict[letter] = 1
            t_dict[letter] += 1

        if s_dict.values.sort() == t_dict.values.sort():
            return True
        return False
