class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1 or n == 0:
                return True
            return False
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
        for i in range(1, len(flowerbed)-1): 
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 1 or flowerbed[i+1] == 1:
                    continue 
                else:
                    flowerbed[i] = 1
                    n -= 1
            else:
                continue

        length = len(flowerbed)-1
        if flowerbed[length] == 0 and flowerbed[length-1] == 0:
            n -= 1
        return True if n <= 0 else False 