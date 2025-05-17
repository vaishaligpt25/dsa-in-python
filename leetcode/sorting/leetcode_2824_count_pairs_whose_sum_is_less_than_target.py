# leetcode_2824: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        sorted_nums: List[int] = sorted(nums)

