# leetcode_2733:-https://leetcode.com/problems/neither-minimum-nor-maximum

from typing import List, Set


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1

        nums_sorted: List[int] = sorted(nums)
        return nums_sorted[1]


class SolutionTest:
    def find_neither_min_nor_max(self) -> None:
        soln: Solution = Solution()
        assert soln.findNonMinOrMax(nums=[3, 2, 1, 4]) == 2
        assert soln.findNonMinOrMax(nums=[1, 2]) == -1
        assert soln.findNonMinOrMax(nums=[2, 1, 3]) == 2


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.find_neither_min_nor_max()
