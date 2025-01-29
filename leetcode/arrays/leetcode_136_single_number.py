#leetcode_136:-https://leetcode.com/problems/single-number/description/?envType=problem-list-v2&envId=array

from typing import List, Dict, Set


class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        # create frequency map
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # find num with freq 1
        for num, freq in count.items():
            if freq == 1:
                return num

    def singleNumber2(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                 seen.remove(num)
            else:
                seen.add(num)
        return seen.pop()


class SolutionTest:
    def test_single_number(self) -> None:
        soln: Solution = Solution()
        # assert soln.singleNumber2([4,1,2,1,2]) == 4
        # assert soln.singleNumber2([1]) == 1
        # assert soln.singleNumber2([-1,-1,2]) == 2

        assert soln.singleNumber1([4, 1, 2, 1, 2]) == 4
        assert soln.singleNumber1([1]) == 1
        assert soln.singleNumber1([-1, -1, 2]) == 2

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_single_number()
