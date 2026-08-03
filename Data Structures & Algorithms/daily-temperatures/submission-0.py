class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final_list = []
        i, j = 0, 0
        while j < len(temperatures) and i < len(temperatures):
            if temperatures[i] > temperatures[j]:
                final_list.append(i-j)
                j += 1
                i = j
            i += 1
            
            if i == len(temperatures)-1 and temperatures[i] < temperatures[j]:
                final_list.append(0)
                j += 1
                i = j

        final_list.append(0)
        return final_list