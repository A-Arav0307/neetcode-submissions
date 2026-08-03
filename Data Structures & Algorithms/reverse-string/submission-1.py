class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            return s
        
        s[0], s[-1] = s[-1], s[0]
        self.reverseString(s[1:len(s)-1])