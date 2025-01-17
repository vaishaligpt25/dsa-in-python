#leetcode_628:-https://leetcode.com/problems/maximum-product-of-three-numbers

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
#sort the array in ascending order
        nums.sort()
#Two possible cases:
#1. product of three largest numbers
#2. product of two smallest numbers(if negative) and largest number
        return max(nums[-1] * nums[-2] * nums[-3],  # case 1
                   nums[0] * nums[1] *nums[-1])     # case 2



class SolutionTest:
    def test_maximumProduct(self):
        soln: Solution = Solution()
        assert soln.maximumProduct([1,2,3]) == 6
        assert soln.maximumProduct([-1,-2,-3,4]) == 24
        assert soln.maximumProduct([-100, -98, 1,2,3,4]) ==39200
        assert soln.maximumProduct([-1, -2, -3]) == -6



if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_maximumProduct()

