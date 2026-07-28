class Solution:
    def myPow(self, x: float, n: int) -> float:
        val = 1
        if n == 0: 
            return 1 
        if n > 0: 
            for i in range(n): 
                val *= x

        if n < 0: 
            for i in range(abs(n)): 
                val *= x
            val = 1/val    

        return val