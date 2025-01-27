# leetcoe_1909:-https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing

from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def is_strictly_increasing(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i-1]:
                    return False
            return True
        #try removing each element and check if remaining array is strictly increasing.
        for i in range(len(nums)):
            # create new array without element at index i
            temp = nums[:i] + nums[i+1:]
            if is_strictly_increasing(temp):
                return True
        return False


class SolutionTest:
    def canBeIncreasing(self) -> None:
        soln: Solution = Solution()
        assert soln.canBeIncreasing(nums = [1,2,10,5,7]) == True
        assert soln.canBeIncreasing(nums = [2,3,1,2]) == False


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.canBeIncreasing()
