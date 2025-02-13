# https://leetcode.com/problems/k-closest-points-to-origin

from typing import List
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_from_origin: List[float] = self._distance_from_origin(points=points)
        zip_pair: List[tuple[float, List[int]]] = self._zip_distance_and_pair(distances=distance_from_origin, points=points)
        zip_pair_sorting = sorted(zip_pair, key=lambda x:x[0])
        result: List[List[int]] = self._separate_pairs_from_zip(my_pair=zip_pair_sorting)
        return result[:k]

    def _distance_from_origin(self, points: List[List[int]]) -> List[float]:
        distances = []
        for point in points:
          distance: float = math.sqrt(point[0] * point[0] + point[1] * point[1])
          distances.append(distance)
        return distances

        # return [math.sqrt(point[0] * point[0] + point[1] * point[1]) for point in points]

    def _zip_distance_and_pair(self, distances: List[float], points: List[List[int]]) -> List[tuple[float,List[int]]]:
        # return [(distances, points) for distances, point in zip(distances, points)]
        return list(zip(distances, points))

    def _separate_pairs_from_zip(self, my_pair: List[tuple[float, List[int]]]) -> List[List[int]]:
        return [pair[1] for pair in my_pair]

    #------------------------------------------------

    def kClosest1(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])[:k]


class SolutionTest:
    def closest_points(self) -> None:
        soln: Solution = Solution()
        assert soln.kClosest(points = [[1,3],[-2,2]], k = 1) == [[-2,2]]
        assert soln.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2) == [[3,3],[-2,4]]

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.closest_points()
