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
        j = 0
        while i < len(s):
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            string = s[j:j+length]
            final_list.append(string)

            j += length
            i = j

        return final_list

