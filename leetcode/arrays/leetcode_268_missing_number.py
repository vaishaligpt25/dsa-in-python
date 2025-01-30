#leetcode_268https://leetcode.com/problems/missing-number/description/?envType=problem-list-v2&envId=array

from typing import List, Dict, Set


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort() # sort the array

        # check if zero is missing at the start
        if nums[0] != 0:
            return 0

        #check for missing number in between
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                return nums[i - 1] + 1

        #if no number is missing in between, then the missing number is n
        return len(nums)

    def missingNumber1(self, nums: List[int]) -> int:
        # create a set from input array
        num_set = set(nums)

        #check each number from 0 to n
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
        return -1

    def missingNumber2(self, nums: List[int]) -> int:
        # create a hash map
        num_map = {}

        #add all numbers to hash map
        for num in nums:
            num_map[num] = True

        # check for missing number from 0 to n
        for i in range(len(nums) + 1):
            if i not in num_map:
                return i
        return -1


class SolutionTest:
    def check_missing_number(self) -> None:
        soln: Solution = Solution()
        assert soln.missingNumber2(nums=[0,1]) == 2
        assert soln.missingNumber2(nums=[0, 1, 3, 4]) == 2
        assert soln.missingNumber2(nums=[0]) == 1


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_missing_number()