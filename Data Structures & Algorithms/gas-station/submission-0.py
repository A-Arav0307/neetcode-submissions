class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 
        # [1,2,3,4]
        # [2,2,4,1]
        # [-1,-1,-2,1]
        diff = [a - b for a, b in zip(gas, cost)] 
        res = 0
        for i in range(len(gas)):
            if diff[i] < 0: 
                continue 
            res = i
            
        return res
        
