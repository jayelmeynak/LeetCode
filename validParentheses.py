class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for a in s:
            if a == '(' or a == '[' or a == '{':
                stack.append(a)
            elif a == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif a == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif a == '}' and stack and stack[-1] == '{':
                stack.pop()
            else: return False
        if len(stack) == 0:
            return True
        else:
            return False