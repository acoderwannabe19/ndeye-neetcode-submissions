class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            elif i == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(a+b)
            elif i == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif i == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(a*b)
            elif i == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))

            
        return stack[0]
        