from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        r = i = 0
        while (i < len(chars)):
            currChar = chars[i]
            curr_occ = 0
            while ((i < len(chars)) and (chars[i] == currChar)):
                curr_occ += 1
                i += 1
            chars[r] = currChar
            r += 1
            if (curr_occ > 1):
                curr_occ_str = str(curr_occ)
                for j in range(len(curr_occ_str)):
                    chars[r] = curr_occ_str[j]
                    r += 1
        return r

    def compress2(self, chars: List[str]) -> str:
        ans = []
        i = 0
        while (i < len(chars)):
            currChar = chars[i]
            curr_occ = 0
            while i < len(chars) and chars[i] == currChar:
                curr_occ += 1
                i += 1
            ans.append(currChar)
            if (curr_occ > 1):
                curr_occ_str = str(curr_occ)
                ans.append(curr_occ_str)
        return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.compress2(["a", "a", "b", "b", "c", "c", "c"]))
