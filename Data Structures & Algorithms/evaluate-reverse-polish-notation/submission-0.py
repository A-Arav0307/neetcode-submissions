class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens: 
            if char not in ('/', '+', '*', '-'):
                stack.append(char)
            if char == '+': 
                stack[-2] = str(int(stack[-1]) + int(stack[-2]))
                stack.pop()
            if char == '-': 
                stack[-2] = str(int(stack[-2]) - int(stack[-1]))
                stack.pop()
            if char == '*': 
                stack[-2] = str(int(stack[-1]) * int(stack[-2]))
                stack.pop()
            if char == '/': 
                stack[-2] = str(int(stack[-2]) / int(stack[-1]))
                stack.pop()

        return int(stack[0])