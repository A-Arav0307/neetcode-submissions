class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)

        n = len(s)

        if len(s) == 1:
            if s[0] == '0':
                return 0
            return 1

        if s[n-1] != '0':
            dp[n-1] = 1

        if int(s[n-2]) == 2:
            if int(s[n-1]) > 6:
                dp[n-2] = 1
            if int(s[n-1]) <= 6:
                dp[n-2] = 1 + dp[n-1]
        
        elif int(s[n-2]) == 1:
            dp[n-2] = 1 + dp[n-1]
 

        if len(s) == 2:
            return dp[n-2]

        for i in range(len(s)-3, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            
            if int(s[i]) > 0 and int(s[i]) <= 2:
                dp[i] = 1 + dp[i+1]

        return dp[0]

        
        