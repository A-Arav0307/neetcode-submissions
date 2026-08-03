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


        for key1, value1 in final_dict_s.items():
            for key2, value2 in final_dict_t.items():
                if key1 in final_dict_t.keys():
                    if final_dict_s[key1] == final_dict_t[key2]:
                        continue
                    else:
                        return False


                if key1 not in final_dict_t.keys():
                    return False
        return True
            

        
        


        
        