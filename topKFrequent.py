from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        freq = [0] * (len(nums) + 1)
        for num in dic:
            if freq[dic[num]] == 0:
                freq[dic[num]] = [num]
            else:
                freq[dic[num]].append(num)
        ans = []
        for i in range(len(nums), -1, -1):
            if freq[i] != 0:
                ans.extend(freq[i])
            if len(ans) == k:
                return ans

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,2,3,4,5], 3))
