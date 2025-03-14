from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                a2 = stack.pop()
                a1 = stack.pop()
                stack.append(a1 - a2)
            elif token == "/":
                a2 = stack.pop()
                a1 = stack.pop()
                stack.append(int(a1 / a2))
            else:
                stack.append(int(token))
        return stack.pop()
if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))