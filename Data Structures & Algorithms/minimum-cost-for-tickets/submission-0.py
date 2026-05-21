class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #costs[0] is 1 day
        #costs[1] is 7 day
        #costs[2] is 30 day
        n = len(days)
        dp = [0] * (n+1)
        dp[n-1] = costs[0]
        for i in range(n-1, -1, -1):
            #1 day ticket
            j = i
            while j < n and days[j] < days[i] + 1:
                j += 1
            one_day = costs[0] + dp[j]
            
            #7 day ticket
            while j < n and days[j] < days[i] + 7:
                j += 1
            seven_day = costs[1] + dp[j]

            #30 day ticket
            while j < n and days[j] < days[i] + 30:
                j += 1
            thirty_day = costs[2] + dp[j]

            dp[i] = min(one_day, seven_day, thirty_day)

        return dp[0]