class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                num = stack.pop() + stack.pop()
                stack.append(num)
            elif c == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                num = num1 - num2
                stack.append(num)
            elif c == '*':
                num = stack.pop() * stack.pop()
                stack.append(num)
            elif c == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                num = num1 / num2
                stack.append(int(num))
            else:
                stack.append(int(c))
        
        return stack[0]

            
        