# leetcode_169_https://leetcode.com/problems/majority-element/description
from typing import List, Dict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > len(nums) // 2:
                return num
        return nums[0]
