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

        for s_val in s_dict.values():
            final_s_values.append(s_val)

        for t_val in t_dict.values():
            final_t_values.append(t_val)

        final_s_values.sort()
        final_t_values.sort()

        if final_s_values == final_t_values:
            return True
        return False
