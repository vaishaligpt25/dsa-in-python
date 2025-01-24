# leetcode_2923:-https://leetcode.com/problems/find-champion-i

from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        return None

    def method_1(self, grid: List[List[int]]) -> int:
        n: int = len(grid)

        for i in range(n):
            if all(grid[i][j] == 1 for j in range(n) if i != j):
                return i
        return -1

    def method_2(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        for i in range(n):
            is_champion: bool = True

            for j in range(n):
                if i != j and grid[i][j] == 0:
                    is_champion = False
                    break

            if is_champion:
                return i
        return -1


class SolutionTest:
    def findChampion(self) -> None:
        soln: Solution = Solution()
        assert soln.method_2(grid=[[0,1],[0,0]]) == 0
        assert soln.method_2(grid = [[0,0,1],[1,0,1],[0,0,0]]) == 1


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.findChampion()


