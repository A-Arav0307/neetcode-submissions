class Solution:
    def isHappy(self, n: int) -> bool:
        val = n
        visited = set()
        def helper(number): 
            val = 0 
            for n in str(number):
                val += int(n) ** 2 

            return val

        while val not in visited:
            val = helper(val) 
            if val == 1: 
                return True 
            visited.add(val) 


        return False