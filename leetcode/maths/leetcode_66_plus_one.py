# leetcode_66:-https://leetcode.com/problems/plus-one

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # start from the rightmost digit
        for i in range(n - 1, -1, -1):
          # If digit is less than 9, simply increment and return
           if digits[i] < 9:
               digits[i] += 1
               return digits
          # if digit is 9, make it 0 and continue to next digit
           digits[i] = 0

        # if all digits were 9, add 1 at the beginning
        return [1] + digits


class SolutionTest:
    def test_plusOne(self):
        solution = Solution()
        assert solution.plusOne([1,2,3]) == [1, 2, 4]
        assert solution.plusOne([9]) == [1,0]
        assert solution.plusOne([4,3,2,1]) == [4, 3, 2, 2]
        assert solution.plusOne([9,9,9]) == [1,0,0,0]



if __name__ == '__main__':
    solution_test: SolutionTest = SolutionTest()
    solution_test.test_plusOne()





