from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        while len(s) > 0:
            check_el = s[0]
            res.append(s[0:s.rfind(check_el) + 1])
            s = s[s.rfind(check_el) + 1:]
            individ_els = set(i for i in res[-1])
            while len(individ_els) > 0:
                individ_el = individ_els.pop()
                index_individ_el = s.rfind(individ_el)
                if index_individ_el >= 0:
                    res[-1] = [*res[-1], *s[:index_individ_el + 1]]
                    for el_el in s[:index_individ_el + 1]:
                        if el_el != individ_el:
                            individ_els.add(el_el)
                    s = s[index_individ_el + 1:]
            res[-1] = len(res[-1])
        return res
