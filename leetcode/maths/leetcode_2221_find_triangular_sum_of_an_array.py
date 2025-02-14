# https://leetcode.com/problems/find-triangular-sum-of-an-array

from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n - 1):  # For each row of the triangle
            for j in range(n - 1 - i):  # Process elements in current row
                nums[j] = (nums[j] + nums[j + 1]) % 10
        return nums[0]


class SolutionTest:
    def test_traingular_sum(self) -> None:
        soln: Solution = Solution()
        assert soln.triangularSum(nums = [1,2,3,4,5]) == 8
        assert soln.triangularSum(nums = [5]) == 5


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_traingular_sum()
