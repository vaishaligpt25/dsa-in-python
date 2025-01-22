# leetcode_2133:-https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers

from typing import List, Set

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n: int = len(matrix)

        # check each row
        for row in matrix:
            row_set: Set[int] = set()
            for num in row:
                if num < 1 or num > n or num in row_set:
                    return False
                row_set.add(num)

        # check each column
        for col in range(n):
            col_set: Set[int] = set()
            for row in range(n):
                num = matrix[row][col]
                if num < 1 or num > n or num in col_set:
                    return False
                col_set.add(num)
        return True

class SolutionTest:
    def test_checkValid(self) -> None:
        soln: Solution = Solution()

        assert soln.checkValid([[1,2,3],[3,1,2],[2,3,1]]) == True
        assert soln.checkValid([[1,1,1],[1,2,3],[1,2,3]]) == False

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_checkValid()
