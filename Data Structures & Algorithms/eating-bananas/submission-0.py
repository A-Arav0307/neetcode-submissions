import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        

        while l <= r: 
            middle = (l+r) // 2
            time = 0
            for num in piles: 
                time += math.ceil(num / middle)
            if time > h:
                l = middle + 1

            else:
                r = middle - 1
        return l