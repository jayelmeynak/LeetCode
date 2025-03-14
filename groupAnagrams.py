from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams_dict = defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            anagrams_dict[sorted_str].append(string)
        for anagrams in anagrams_dict.values():
            res.append(anagrams)

        return res
