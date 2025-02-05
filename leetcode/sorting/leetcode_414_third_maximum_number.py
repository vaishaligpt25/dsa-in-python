# leetcode_414:-https://leetcode.com/problems/third-maximum-number

from typing import List, Set


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_sorted: List[int] = sorted(set(nums), reverse= True)

        # If less than 3 unique numbers, return maximum
        if len(nums_sorted) < 3:
            return nums_sorted[0]

        # Return third maximum
        return nums_sorted[2]


def thirdMax1(self, nums: List[int]) -> int:
    nums_set: set[int] = set(nums)

    # If less than 3 unique numbers, return maximum
    if len(nums_set) < 3:
        return max(nums_set)

    # Convert to sorted list and return third element
    return sorted(nums_set, reverse=True)[2]


class SolutionTest:
    def max_number(self) -> None:
        soln: Solution = Solution()
        assert soln.thirdMax(nums = [3,2,1]) == 1
        assert soln.thirdMax(nums = [1,2]) == 2


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.max_number()
