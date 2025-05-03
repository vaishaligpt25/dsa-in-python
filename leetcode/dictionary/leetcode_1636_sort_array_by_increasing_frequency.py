# leetcode_1636_https://leetcode.com/problems/sort-array-by-increasing-frequency/
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return sorted(nums, key=lambda x: (freq[x], -x))

class SolutionTest:
    def check_frequencySort(self) -> None:
        soln: Solution = Solution()
        assert soln.frequencySort(nums = [1,1,2,2,2,3]) == [3,1,1,2,2,2]
        assert soln.frequencySort(nums = [2,3,1,3,2]) == [1,3,3,2,2]
        assert soln.frequencySort(nums = [-1,1,-6,4,5,-6,1,4,1]) == [5,-1,4,4,-6,-6,1,1,1]


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_frequencySort()