class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        idx = 0
        while idx < len(tokens):
            if tokens[idx] == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif tokens[idx] == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif tokens[idx] == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif tokens[idx] == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(tokens[idx]))
            idx += 1
        return stack[-1]