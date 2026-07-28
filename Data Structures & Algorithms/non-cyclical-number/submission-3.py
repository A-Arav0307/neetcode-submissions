class Solution:
    def isHappy(self, n: int) -> bool:
        val = n
        visited = set()
        def helper(number): 
            val = 0 
            for n in str(number):
                val += int(n) ** 2 

            return val

        while n != 1 and n not in visited:
            visited.add(n)
            n = helper(n)


        return n == 1