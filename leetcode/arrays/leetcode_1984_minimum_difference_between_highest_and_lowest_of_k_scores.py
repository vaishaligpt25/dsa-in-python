# leetcode_1984_https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))

    def minimumDifference1(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        min_diff: float = float('inf')
        for i in range(len(nums) - k + 1):
            current_diff: int = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, current_diff)
        return min_diff


