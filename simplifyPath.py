class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for char in path + "/":
            if char == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += char
        return "/" + "/".join(stack)


if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath("/home/user/Documents/../Pictures"))
