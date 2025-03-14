class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7: return True

        seen = set()
        while n != 1 and n != 7:
            if n in seen:
                return False
            seen.add(n)
            n = sum(int(c) ** 2 for c in str(n))
        return True
