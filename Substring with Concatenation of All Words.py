from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        frq = {}
        for word in words:
            frq[word] = frq.get(word, 0) + 1
        len_s = len(s)
        n = len(words)
        word_len = len(words[0])
        window_len = word_len * len(words)
        ans = []
        for star_pos in range(word_len):
            start = star_pos
            while True:
                cur_frq = frq.copy()
                match = True
                for i in range(n):
                    curr_word = s[start + i * word_len:start+(i+1)*word_len]
                    if curr_word not in cur_frq:
                        match = False
                        break
                    if cur_frq[curr_word] == 0:
                        match = False
                        break
                    cur_frq[curr_word] = cur_frq.get(curr_word, 0) - 1
                if match:
                    ans.append(start)
                start += word_len
                if start + window_len > len_s:
                    break
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))