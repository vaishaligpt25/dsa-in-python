# leetcode_1480https://leetcode.com/problems/running-sum-of-1d-array

from typing import List, Set, Dict


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # create prefix sum array
        prefix_sum = [nums[0]]  # Initialize with first element

        # build prefix sum array
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        return prefix_sum

    # In- place prefix sum


def runningSum1(self, nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


class SolutionTest:
    def test_running_sum(self) -> None:
        soln: Solution = Solution()
        assert soln.runningSum(nums=[1, 2, 3, 4]) == [1,3,6,10]
        assert soln.runningSum(nums=[1, 5, 3, 4]) == [1, 6, 9, 13]

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_running_sum()