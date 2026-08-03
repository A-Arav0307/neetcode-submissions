class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0
        def solution(n, ways):
            if n == 0: 
                return ways

            else: 
                return solution(n-1, int(ways + n/n)) 

        return solution(n, ways)

