from typing import  List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if self.count_digits(num) % 2 == 0)

    def count_digits(self, num: int) -> int:
        if num == 0: # Handle zero case
            return 1
        count = 0
        while num: #while number is not zero
            count += 1
            num = int (num / 10)  #remove last digit
        return count


class SolutionTest:
    def test_findNumbers(self) -> None:
        soln: Solution = Solution()

        assert soln.findNumbers(nums=[12,345,2,6,7896]) == 2
        assert soln.findNumbers([555,901,482,1771]) == 1
        assert soln.findNumbers([12,111,3456,2,23]) == 3
        assert soln.findNumbers([]) == 0
        assert soln.findNumbers([1]) == 0



if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_findNumbers()
