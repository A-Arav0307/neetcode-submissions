class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for character in tokens: 
            if character not in ('/', '+', '*', '-'):
                stack.append(character)
            elif character == '+': 
                stack[-2] = str(int(stack[-1]) + int(stack[-2]))
                stack.pop()
            elif character == '-': 
                stack[-2] = str(int(stack[-2]) - int(stack[-1]))
                stack.pop()
            elif character == '*': 
                stack[-2] = str(int(stack[-1]) * int(stack[-2]))
                stack.pop()
            elif character == '/': 
                stack[-2] = str(int(stack[-2]) // int(stack[-1]))
                stack.pop()

        return int(stack[0])