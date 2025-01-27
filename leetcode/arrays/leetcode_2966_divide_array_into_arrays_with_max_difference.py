# leetocde_2966:-https://leetcode.com/problems/divide-array-into-arrays-with-max-difference

from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        sorted_list: List[int] = sorted(nums)
        return self._check_difference(sorted_list=sorted_list,k=k)

    # # check if array length is divisible by 3
    #     if len(nums) % 3 != 0:
    #      return []



    def _check_difference(self, sorted_list: List[int], k: int) -> List[List[int]]:
        result = []

        for i in range(0, len(sorted_list),3):
            max_value: int = sorted_list[i + 2]
            min_value: int = sorted_list[i]
            mid_value = sorted_list[i + 1]

            if max_value - min_value > k:
                return []

            result.append([min_value, mid_value, max_value])

        return result


class SolutionTest:

    def _check_difference(self) -> None:
        soln: Solution = Solution()

        assert soln._check_difference(sorted_list= [1, 1, 3, 3, 4, 5, 7, 8, 9],k= 4) == [[1,1,3], [3,4,5], [7,8,9]]
        assert soln._check_difference(sorted_list=[1, 1, 3, 3, 4, 5, 7, 8, 9], k=3) == [[1, 1, 3], [3, 4, 5], [7, 8, 9]]
        assert soln._check_difference(sorted_list=[1, 1, 3, 3, 4, 5, 7, 8, 9], k=2) == [[1, 1, 3], [3, 4, 5], [7, 8, 9]]
        assert soln._check_difference(sorted_list=[1, 1, 3, 3, 4, 5, 7, 8, 9], k=1) == []


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test._check_difference()