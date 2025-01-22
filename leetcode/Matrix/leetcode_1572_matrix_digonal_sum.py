# leetcode_1572:-https://leetcode.com/problems/matrix-diagonal-sum

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return self.diagonal_sum_method2(mat)


    def diagonal_sum_method1(self,mat: List[List[int]]) -> int:
        #get matrix size:
        n: int = len(mat)
        total: int = 0

        #add primary diagonal elements
        for i in range(n):
            total += mat[i][i]

        #add secondary diagonal elements
        for i in range(n):
            #skip if it's centre element already counted
            if i != n - 1 - i:
               total += mat[i][n-1-i]

        return total

   #-----------2nd method---------

    def diagonal_sum_method2(self,mat: List[List[int]]) ->int:
        n: int = len(mat)
        total: int = 0

        for i in range(n):
            # add primary diagonal
            total += mat[i][i]

            # add secondary diagonal (if not overlapping)
            if i != n-1-i:
                total += mat[i][n-1-i]

        return total

class SolutionTest:
    def test_diagonalSum(self) -> None:
        soln: Solution = Solution()

        assert soln.diagonalSum([[1,2,3],
                  [4,5,6],
                  [7,8,9]]) == 25

        assert soln.diagonalSum([[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]]) == 8

        assert soln.diagonalSum([[5]]) == 5


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_diagonalSum()





