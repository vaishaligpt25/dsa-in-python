# leetcode_2319:-https://leetcode.com/problems/check-if-matrix-is-x-matrix/

from typing import List

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        return self._check_x_matrix_method_2(grid=grid)

    def _check_x_matrix_method_1(self, grid: List[List[int]]) -> bool:
        n: int = len(grid)

        for i in range(n):
            for j in range(n):
                # check diagonal element
                is_diagonal = (i == j) or (i + j == n - 1)
                if is_diagonal:
                    # diagonal element must be zero
                    if grid[i][j] == 0:
                        return False
                else:
                    # Non-diagonal element must be zero
                    if grid[i][j] != 0:
                        return False

            return True


    def _check_x_matrix_method_2(self, grid: List[List[int]]) -> bool:
        n: int = len(grid)

        for i in range(n):
            for j in range(n):
                if (i == j) or (i + j == n - 1):
                    # diagonal element must be nonzero
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] != 0:
                    # non-diagonal element must be zero
                    return False

            return True


class SolutionTest:
    def checkXMatrix(self) -> None:
        soln: Solution = Solution()
        assert soln._check_x_matrix_method_2([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]) == True
        assert soln._check_x_matrix_method_2([[5,7,0],[0,3,1],[0,5,0]]) == False
        assert soln._check_x_matrix_method_2([[1,2], [3,1]]) == True


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.checkXMatrix()







