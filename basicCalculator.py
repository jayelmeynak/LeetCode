import re
from typing import List

#
# class Solution:
#     def calculate(self, s: str) -> int:
#         s = s.replace(" ", "")
#         if s.isdigit():
#             return int(s)
#         for i in range(len(s)):
#             if i == 0 and s[i] == '-':
#                 s = '0' + s
#             elif s[i] == '-' and s[i - 1] == '(':
#                 s = s[:i] + '0' + s[i:]
#
#         def parse_expression(s: str) -> list:
#             tokens = re.findall(r'\d+|[+\-*/()]', s)
#             return tokens
#
#         new_s = parse_expression(s)
#
#         def infToPostfix(a: List[str]) -> List[str]:
#             ans = []
#             stack = []
#             weight = {'+': 1, '-': 1, '*': 2, '/': 2}
#             for char in a:
#                 if char.isdigit():
#                     ans.append(char)
#                 elif char in weight:
#                     if not stack:
#                         stack.append(char)
#                         continue
#                     elif stack[-1] == '(':
#                         stack.append(char)
#                         continue
#                     while stack and ((stack[-1] in weight and weight[char] <= weight[stack[-1]]) or stack[-1] != '('):
#                         ans.append(stack.pop())
#                     stack.append(char)
#                 elif char == '(':
#                     stack.append(char)
#                 elif char == ')':
#                     while stack and stack[-1] != '(':
#                         ans.append(stack.pop())
#                     stack.pop()
#             while stack:
#                 ans.append(stack.pop())
#             return ans
#
#         new_str = infToPostfix(new_s)
#         stack = []
#         for char in new_str:
#             if char.isdigit():
#                 stack.append(int(char))
#             elif char == "+":
#                 stack.append(stack.pop() + stack.pop())
#             elif char == "*":
#                 stack.append(stack.pop() * stack.pop())
#             elif char == "-":
#                 a2 = stack.pop()
#                 a1 = stack.pop()
#                 stack.append(a1 - a2)
#             elif char == "/":
#                 a2 = stack.pop()
#                 a1 = stack.pop()
#                 stack.append(int(a1 / a2))
#         return stack.pop()

"""
GPT
"""


# def apply_op(operators, values):
#     op = operators.pop()
#     b = values.pop()
#     a = values.pop()
#     if op == '+':
#         values.append(a + b)
#     elif op == '-':
#         values.append(a - b)
#     elif op == '*':
#         values.append(a * b)
#     elif op == '/':
#         values.append(int(a / b))
#
# def greater_or_equal_precedence(op1, op2):
#     precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
#     return precedence[op1] >= precedence[op2]
#
# class Solution:
#     def calculate(self, s: str) -> int:
#         s = s.replace(" ", "")
#         tmp = []
#         for i, ch in enumerate(s):
#             if ch == '-' and (i == 0 or s[i-1] == '('):
#                 tmp.append('0')
#             tmp.append(ch)
#         s = ''.join(tmp)
#
#         operators = []
#         values = []
#         i = 0
#         n = len(s)
#
#         while i < n:
#             ch = s[i]
#             if ch == '(':
#                 operators.append(ch)
#                 i += 1
#             elif ch == ')':
#                 while operators and operators[-1] != '(':
#                     apply_op(operators, values)
#                 operators.pop()  # Удаляем '('
#                 i += 1
#             elif ch in '+-*/':
#                 while operators and operators[-1] != '(' and greater_or_equal_precedence(operators[-1], ch):
#                     apply_op(operators, values)
#                 operators.append(ch)
#                 i += 1
#             else:
#                 num_start = i
#                 while i < n and s[i].isdigit():
#                     i += 1
#                 number = int(s[num_start:i])
#                 values.append(number)
#         while operators:
#             apply_op(operators, values)
#         return values.pop()

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        sign = 1
        result = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '+':
                result += sign * current_num
                current_num = 0
                sign = 1
            elif char == '-':
                result += sign * current_num
                current_num = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * current_num
                current_num = 0
                result *= stack.pop()
                result += stack.pop()

        result += sign * current_num
        return result


if __name__ == "__main__":
    calc = Solution()
    expressions = [
        "(1+(4+5+2)-3)+(6+8)",
        # "2-1+2",
        # "(1)",
        # "1+1",
        # "- (3 + (4 + 5))",
    ]
    for expr in expressions:
        print(f"Выражение: {expr}")
        print(f"Результат: {calc.calculate(expr)}")
        print("---")
