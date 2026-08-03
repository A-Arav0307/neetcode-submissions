class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for character in tokens: 
            if character not in ('/', '+', '*', '-'):
                stack.append(int(character))
            else:
                val2 = int(stack.pop())
                val1 = int(stack.pop())

                if character == '/':
                    stack.append(str(val1 / val2))
                elif character == '*':
                    stack.append(str(val1 * val2))
                elif character == '-':
                    stack.append(str(val1 - val2))
                else:
                    stack.append(str(val1 + val2))

        return int(stack[0])