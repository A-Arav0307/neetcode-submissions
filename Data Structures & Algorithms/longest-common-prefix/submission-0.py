class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = ''
        length = len(strs[0])
        for word in strs:
            length = min(length, len(word))

        j = 0
        while j < length:
            for i in range(len(strs)-1):
                if strs[i][j] != strs[i+1][j]:
                    return res
            res += strs[0][j]
            j += 1

        return res
                
            


        