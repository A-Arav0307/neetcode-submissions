class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []
        new_a, new_b, new_c = float('-inf'), float('-inf'), float('-inf')
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            else:
                valid.append([a,b,c])
   
        for a, b, c in valid:
            new_a = max(new_a, a) 
            new_b = max(new_b, b) 
            new_c = max(new_c, c) 

    
        if [new_a, new_b, new_c] == target:
            return True
        return False