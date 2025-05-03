# leetcode_1636_https://leetcode.com/problems/sort-array-by-increasing-frequency/
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return sorted(nums, key=lambda x: (freq[x], -x))

