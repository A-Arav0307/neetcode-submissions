from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False 

        frequency = defaultdict(int)
        for num in hand:
            frequency[num] += 1
        # size = 4
        # {1:inf, 2:1, 3:1, 4:2, 5:1}
        # {1:1, 2:1, 3:2, 4:1, 5:1, 6:1, 7:1}

        for i in range(len(hand) // groupSize):
            min_val = min(frequency.keys())
            size = 0
            while size != groupSize:
                if min_val not in frequency or frequency[min_val] == float('inf'):
                    return False
                size += 1
                frequency[min_val] -= 1
                if frequency[min_val] == 0:
                    del frequency[min_val]
                min_val += 1

        return True