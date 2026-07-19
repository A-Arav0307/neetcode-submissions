class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final_list = [0] * len(temperatures)
        stack = [] # [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                final_list[stackI] = i - stackI

            stack.append((t,i))
        return final_list