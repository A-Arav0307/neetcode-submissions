class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs: 
            new_word = str(len(word)) + '#' + word
            string += new_word
        return string
        
    def decode(self, s: str) -> List[str]:
        final_list = []
        i = 0
        j = 2
        while i < len(s):
            length = int(s[i])
            string = s[j:j+length]
            final_list.append(string)
            j += length
            i = j
            j += 2
        return final_list
