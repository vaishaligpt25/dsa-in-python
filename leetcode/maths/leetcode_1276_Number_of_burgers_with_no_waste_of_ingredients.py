# leetcode_1276:- https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients

from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        return self._num_of_jumbo_and_small_burger(num_of_cheeseSlices=cheeseSlices, num_of_tomatoSlices=tomatoSlices)

    def _num_of_jumbo_and_small_burger(self, num_of_tomatoSlices: int, num_of_cheeseSlices: int) -> List[int]:
        total_num_of_jumbo_burger: int = int((num_of_tomatoSlices - (2 * num_of_cheeseSlices)) / 2)
        if total_num_of_jumbo_burger < 0:
            return []

        total_num_of_small_burger: int = int(((4 * num_of_cheeseSlices) - num_of_tomatoSlices) / 2)
        if total_num_of_small_burger < 0:
            return []

        condition_1_check: bool = (total_num_of_jumbo_burger + total_num_of_small_burger) == num_of_cheeseSlices
        condition_2_check: bool = (4* total_num_of_jumbo_burger + 2* total_num_of_small_burger) == num_of_tomatoSlices
        if condition_1_check and condition_2_check:
            return [total_num_of_jumbo_burger, total_num_of_small_burger]
        else:
            return []








class SolutionTest:
    def test__num_of_jumbo_and_small_burger(self) -> None:
        soln: Solution = Solution()
        num_of_tomatoSlices_in: int
        num_of_cheeseSlices_in: int
        result_out_expected: List[int]
        result_out_computed: List[int]

        num_of_tomatoSlices_in = 16
        num_of_cheeseSlices_in = 7
        result_out_expected = [1, 6]
        result_out_computed = soln._num_of_jumbo_and_small_burger(num_of_tomatoSlices=num_of_tomatoSlices_in,
                                                                  num_of_cheeseSlices=num_of_cheeseSlices_in)
        assert result_out_expected == result_out_computed

        num_of_tomatoSlices_in = 17
        num_of_cheeseSlices_in = 4
        result_out_expected = []
        result_out_computed = soln._num_of_jumbo_and_small_burger(num_of_tomatoSlices=num_of_tomatoSlices_in,
                                                                  num_of_cheeseSlices=num_of_cheeseSlices_in)
        assert result_out_expected == result_out_computed

        num_of_tomatoSlices_in = 4
        num_of_cheeseSlices_in = 17
        result_out_expected = []
        result_out_computed = soln._num_of_jumbo_and_small_burger(num_of_tomatoSlices=num_of_tomatoSlices_in,
                                                                  num_of_cheeseSlices=num_of_cheeseSlices_in)
        assert result_out_expected == result_out_computed


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test__num_of_jumbo_and_small_burger()
