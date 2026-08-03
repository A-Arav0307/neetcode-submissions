class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        final_dict_s = {}
        final_dict_t = {}
        for character in s: 
            if character not in final_dict.keys():
                final_dict_s[character] = 1
            else:
                final_dict_s[character] += 1



        for character in t: 
            if character not in final_dict.keys():
                final_dict_t[character] = 1
            else:
                final_dict_t[character] += 1

        occurrence_s = sorted(list(final_dict_s))
        occurrence_t = sorted(list(final_dict_t))
        if occurrence_s == occurrence_t:
            return True
        return False



        
        