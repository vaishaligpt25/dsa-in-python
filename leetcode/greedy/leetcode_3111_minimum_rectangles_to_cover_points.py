# https://leetcode.com/problems/minimum-rectangles-to-cover-points

from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        x_coordinates: List[int] = [point[0] for point in points]
        # x_coordinates: int = []
        # for point in points:
        #     x_coordinates.append(point[0])
        x_coordinates_sorting: List[int] = sorted(x_coordinates)
        return self._swallow_point_till_limit(sorted_list=x_coordinates_sorting,w=w)


    def _swallow_point_till_limit(self, sorted_list: List[int], w: int):

        length: int = len(sorted_list)
        if len(sorted_list) < 1:
            return len

        if sorted_list[length - 1] - sorted_list[0] <= w:
            return 1
        num_rectangles: int = 1
        current_limit = sorted_list[0] + w

        for x in sorted_list:
            if x > current_limit:
                num_rectangles += 1
                current_limit = x + w
        return num_rectangles


class SolutionTest:
    def find_minimum_reactangle(self) -> None:
        soln: Solution = Solution()
        assert soln.minRectanglesToCoverPoints([[1,1],[5,7],[7,1]], w = 1) == 3
        assert soln.minRectanglesToCoverPoints(points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], w = 1) == 2


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.find_minimum_reactangle()