class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 
        # [1,2,3,4]
        # [2,2,4,1]
        # [-1,-1,-2,1]
        diff = []
        total = 0
        for j in range(len(gas)):
            total += gas[j] - cost[j]
            diff.append(total) 
        res = 0
        print(diff) 
        for i in range(len(gas)):
            if diff[i] < 0: 
                continue 
            res = i
            
        return res
        
