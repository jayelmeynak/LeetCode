from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ''.join(map(str, digits))
        num = int(num_str) + 1
        new_digits = [int(digit) for digit in str(num)]
        return new_digits