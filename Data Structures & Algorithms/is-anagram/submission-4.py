class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        final_dict_s = {}
        final_dict_t = {}
        occurrence_s = []
        occurrence_t = []
        for character in s: 
            if character not in final_dict_s.keys():
                final_dict_s[character] = 1
            else:
                final_dict_s[character] += 1


        for value_s in final_dict_s.values():
            occurrence_s.append(value_s)

        for character in t: 
            if character not in final_dict_t.keys():
                final_dict_t[character] = 1
            else:
                final_dict_t[character] += 1

        for value_t in final_dict_t.values():
            occurrence_t.append(value_t)

        occurrence_s.sort()
        occurrence_t.sort()

        if occurrence_s == occurrence_t:
            return True
        return False

        
        


        
        