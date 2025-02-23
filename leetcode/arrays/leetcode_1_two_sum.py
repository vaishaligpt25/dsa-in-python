# leetcode_1:-https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array

from typing import List, Dict, Set


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hash map to store number and its index
        num_map = {}

        # iterate through the array
        for i, num in enumerate(nums):
            diff = target - num

            # if diff exists in map, return both indices
            if diff in num_map:
                return [num_map[diff], i]

            # add current number and index to map
            num_map[num] = i

        return []  # no solution found


class SolutionTest:

    def check_two_sum(self) -> None:
        soln: Solution = Solution()
        assert soln.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
        assert soln.twoSum([3, 2, 4], target=6) == [1, 2]
        assert soln.twoSum(nums=[1, 3, 4], target=8) == []


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_two_sum()
