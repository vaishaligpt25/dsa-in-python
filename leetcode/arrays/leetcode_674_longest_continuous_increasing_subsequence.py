# leetcode_674:https://leetcode.com/problems/longest-continuous-increasing-subsequence
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_count = 1
        current_count = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 1
        return max_count


class SolutionTest:
    def check_findLengthOfLCIS(self) -> None:
        soln: Solution = Solution()
        assert soln.findLengthOfLCIS(nums=[1, 3, 4, 2, 6]) == 3
        assert soln.findLengthOfLCIS(nums=[1, 1, 1, 1, 1]) == 1


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_findLengthOfLCIS()
