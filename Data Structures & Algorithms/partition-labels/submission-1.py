class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = float('-inf')
        last = {}
        res = []
        for i, char in enumerate(s):
            last[char] = i
        
        l = 0
        for i in range(len(s)):
            c = s[i]
            end = max(end, last[c])
            if i == end:
                res.append(i-l) 
                l = i
        res[0] += 1
        return res