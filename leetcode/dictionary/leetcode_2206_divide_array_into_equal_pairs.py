# leetcode_2206_https://leetcode.com/problems/divide-array-into-equal-pairs/description
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for freq in freq.values():
            if freq % 2 != 0:
                return False
        return True


class SolutionTest:
    def check_divideArray(self) -> None:
        soln: Solution = Solution()
        assert soln.divideArray(nums = [3,2,3,2,2,2]) == True
        assert soln.divideArray(nums = [1,2,3,4]) == False

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_divideArray()