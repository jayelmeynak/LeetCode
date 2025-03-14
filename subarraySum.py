from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1} # словарь позволяет учитывать префикс суммы в которых есть отриц элементы
        # set_arr = set() если бы в nums не было отриц чисел
        res = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in dic:
               res += dic[cur_sum - k]
            dic[cur_sum] = dic.get(cur_sum, 0) + 1
        return res

# 1 1 1 1 1 1 1
# k = 3