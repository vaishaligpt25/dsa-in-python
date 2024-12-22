# LeetCode-1399: https://leetcode.com/problems/count-largest-group

from typing import Dict, List
from itertools import count


class Solution:
    def _calculate_sum_of_digits(self, n: int) -> int:
        # return sum(list(map(int, str(n))))
        return sum([int(d) for d in str(n)])

    def _build_list_of_integers_1_to_n(self, n: int) -> List[int]:
        return list(range(1, n + 1))

    def _convert_to_sum_of_digits(self, my_list: List[int]) -> List[int]:
        # return list(map(lambda n: self._calculate_sum_of_digits(n=n), my_list))
        return [self._calculate_sum_of_digits(n=n) for n in my_list]

    def _build_frequency_dict(self, my_list: List[int]) -> Dict[int, int]:
        frequency_dict: Dict[int, int] = dict()
        for ele in my_list:
            current_frequency: int = frequency_dict.get(ele, 0)
            frequency_dict[ele]: int = current_frequency + 1
        return frequency_dict

    def _find_max_value(self, my_dict: Dict[int, int]) -> int:
        if len(my_dict) == 0:
            return 0
        # if not my_dict:
        #     return 0

        # max_freq: int = 0
        # for key, value in enumerate(my_dict):
        #     max_freq: int = max(max_freq, value)
        # return max_freq
        # return max([value for value in my_dict.values()])
        return max(my_dict.values())

    def _find_frequency_of_value(self, my_dict: Dict[int, int], my_value: int) -> int:
        return len([value for value in my_dict.values() if value == my_value])

    def countLargestGroup(self, n: int) -> int:
        list_of_integers_1_to_n: List[int] = self._build_list_of_integers_1_to_n(n=n)
        list_of_sum_of_digits: List[int] = self._convert_to_sum_of_digits(my_list=list_of_integers_1_to_n)

        frequency_dict: Dict[int, int] = self._build_frequency_dict(my_list=list_of_sum_of_digits)
        maximum_frequency: int = self._find_max_value(my_dict=frequency_dict)

        return self._find_frequency_of_value(my_dict=frequency_dict, my_value=maximum_frequency)


class SolutionTest:
    def test_calculate_sum_of_digits(self) -> None:
        soln: Solution = Solution()

        assert soln._calculate_sum_of_digits(n=97) == 16
        assert soln._calculate_sum_of_digits(n=0) == 0
        assert soln._calculate_sum_of_digits(n=1) == 1
        assert soln._calculate_sum_of_digits(n=673) == 16

    def test_convert_to_sum_of_digits(self) -> None:
        soln: Solution = Solution()

        assert soln._convert_to_sum_of_digits(my_list=[3, 1, 6]) == [3, 1, 6]
        assert soln._convert_to_sum_of_digits(my_list=[13, 143, 68]) == [4, 8, 14]
        assert soln._convert_to_sum_of_digits(my_list=[]) == []
        assert soln._convert_to_sum_of_digits(my_list=[987]) == [24]

    def test_build_frequency_dict(self) -> None:
        soln: Solution = Solution()

        my_list: List[int]
        freq_dict_out_expected: Dict[int, int]
        freq_dict_out_computed: Dict[int, int]

        my_list = [45, 19, 6, 45, 4, 6, 1]
        freq_dict_out_expected = {
            45: 2,
            19: 1,
            6: 2,
            4: 1,
            1: 1
        }
        freq_dict_out_computed = soln._build_frequency_dict(my_list=my_list)
        assert freq_dict_out_expected == freq_dict_out_computed

        my_list = ["cow", "cat", "dog", "cow", "cow", "dog", "pig", "goat"]
        freq_dict_out_expected = {
            "cat": 1,
            "dog": 2,
            "cow": 3,
            "pig": 1,
            "goat": 1
        }
        freq_dict_out_computed = soln._build_frequency_dict(my_list=my_list)
        assert freq_dict_out_expected == freq_dict_out_computed

        my_list = []
        freq_dict_out_expected = {}
        freq_dict_out_computed = soln._build_frequency_dict(my_list=my_list)
        assert freq_dict_out_expected == freq_dict_out_computed

        my_list = [6]
        freq_dict_out_expected = {6: 1}
        freq_dict_out_computed = soln._build_frequency_dict(my_list=my_list)
        assert freq_dict_out_expected == freq_dict_out_computed

    def test_find_max_value(self) -> None:
        soln: Solution = Solution()
        my_dict: Dict[int, int]

        my_dict = {
            45: 2,
            19: 1,
            6: 2,
            4: 1,
            1: 1
        }
        assert soln._find_max_value(my_dict=my_dict) == 2

        my_dict = {
            "cat": 1,
            "dog": 2,
            "cow": 3,
            "pig": 1,
            "goat": 1
        }
        assert soln._find_max_value(my_dict=my_dict) == 3

        my_dict = {45: 2}
        assert soln._find_max_value(my_dict=my_dict) == 2

        my_dict = {}
        assert soln._find_max_value(my_dict=my_dict) == 0

    def test_find_frequency_of_value(self) -> None:
        soln: Solution = Solution()
        my_dict: Dict[int, int]

        my_dict = {
            45: 2,
            19: 1,
            6: 2,
            4: 1,
            1: 1
        }
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=2) == 2
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=1) == 3
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=5) == 0
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value="cow") == 0

        my_dict = {
            "cat": 1,
            "dog": 2,
            "cow": 3,
            "pig": 1,
            "goat": 1
        }
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=2) == 1
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=1) == 3
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=5) == 0
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=3) == 1
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value="cow") == 0

        my_dict = {45: 2}
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=2) == 1
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=1) == 0
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=5) == 0
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=3) == 0
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value="cow") == 0

        my_dict = {}
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=2) == 0
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=1) == 0
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=5) == 0
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value=3) == 0
        assert soln._find_frequency_of_value(my_dict=my_dict, my_value="cow") == 0

    def test_countLargestGroup(self) -> None:
        soln: Solution = Solution()

        assert soln.countLargestGroup(n=13) == 4
        assert soln.countLargestGroup(n=2) == 2


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()

    soln_test.test_calculate_sum_of_digits()
    soln_test.test_convert_to_sum_of_digits()
    soln_test.test_build_frequency_dict()
    soln_test.test_find_max_value()
    soln_test.test_find_frequency_of_value()
    soln_test.test_countLargestGroup()
