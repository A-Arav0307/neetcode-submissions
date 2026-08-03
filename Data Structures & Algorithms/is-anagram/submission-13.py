class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        final_s_values = []
        final_s_keys = []
        final_t_values = []
        final_t_keys = []
        
        for letter in range(len(s)):
            s_letter = s[letter]
            t_letter = t[letter]
            if s_letter not in s_dict:
                s_dict[letter] = 1
            s_dict[letter] += 1

            if t_letter not in t_dict:
                t_dict[letter] = 1
            t_dict[letter] += 1

        for s_key in s_dict.keys():
            final_s_keys.append(s_key)
        final_s_keys.sort()

        for t_key in t_dict.keys():
            final_t_keys.append(t_key)
        final_t_keys.sort()

        for s_val in s_dict.values():
            final_s_values.append(s_val)

        for t_val in t_dict.values():
            final_t_values.append(t_val)

        final_s_values.sort()
        final_t_values.sort()

        if final_s_values == final_t_values and final_s_keys == final_t_keys:
            return True
        return False
