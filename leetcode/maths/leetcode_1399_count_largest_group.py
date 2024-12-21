# LeetCode-1399: https://leetcode.com/problems/count-largest-group

from typing import Dict, List


class Solution:
    def _calculate_sum_of_digits(self, num):
        return sum([int(d) for d in str(num)])

    def _build_freq_map(self, my_list: List[int]) -> Dict[int, int]:
        frequency_map: Dict[int, int] = {}
        for num in my_list:
            crr_frequency: int = frequency_map.get(num, 0)
            frequency_map[num] = crr_frequency + 1
        return frequency_map

    def _build_sum_of_digits_list(self, low: int, high: int) -> List[int]:
        return [self._calculate_sum_of_digits(num) for num in range(low, high + 1)]

    def _build_sum_of_digits_dict(self, low: int, high: int) -> Dict[int, int]:
        sum_of_digits_list: List[int] = self._build_sum_of_digits_list(low, high)
        frequency_map: Dict[int, int] = self._build_freq_map(my_list=sum_of_digits_list)
        return frequency_map

    def _calculate_max_freq(self, freq_map: Dict[int, int]) -> int:
        if not freq_map:
            return 0
        return max(freq_map.values())

    def _count_items_with_freq(self, freq_map: Dict[int, int], freq: int) -> int:
        items_with_freq: List[int] = [key for key, value in freq_map.items() if value == freq]
        num_items: int = len(items_with_freq)
        return num_items

    def countLargestGroup(self, n: int) -> int:
        sum_of_digits_dict: Dict[int, int] = self._build_sum_of_digits_dict(low=1, high=n)
        max_freq: int = self._calculate_max_freq(freq_map=sum_of_digits_dict)
        num_items_with_max_freq: int = self._count_items_with_freq(freq_map=sum_of_digits_dict, freq=max_freq)
        return num_items_with_max_freq


class SolutionTest:
    def test_calculate_sum_of_digits(self) -> None:
        soln: Solution = Solution()

        assert soln._calculate_sum_of_digits(num=0) == 0
        assert soln._calculate_sum_of_digits(num=1) == 1
        assert soln._calculate_sum_of_digits(num=9) == 9
        assert soln._calculate_sum_of_digits(num=10) == 1
        assert soln._calculate_sum_of_digits(num=21) == 3
        assert soln._calculate_sum_of_digits(num=1234567890) == 45

    def test_build_freq_map(self) -> None:
        soln: Solution = Solution()
        my_list_in: List[int]
        freq_map_out_expected: Dict[int, int]
        freq_map_out_calculated: Dict[int, int]

        my_list_in = []
        freq_map_out_expected = {}
        freq_map_out_calculated = soln._build_freq_map(my_list=my_list_in)
        assert freq_map_out_expected == freq_map_out_calculated

        my_list_in = [1, 2, 3, 4, 5]
        freq_map_out_expected = {
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 1
        }
        freq_map_out_calculated = soln._build_freq_map(my_list=my_list_in)
        assert freq_map_out_expected == freq_map_out_calculated

        my_list_in = [1, 2, 3, 2, 1, 0, 9, 1]
        freq_map_out_expected = {
            0: 1,
            1: 3,
            2: 2,
            3: 1,
            9: 1
        }
        freq_map_out_calculated = soln._build_freq_map(my_list=my_list_in)
        assert freq_map_out_expected == freq_map_out_calculated

        my_list_in = [8, 7, 9, 7, 1, -65, 9, -65]
        freq_map_out_expected = {
            -65: 2,
            1: 1,
            7: 2,
            8: 1,
            9: 2
        }
        freq_map_out_calculated = soln._build_freq_map(my_list=my_list_in)
        assert freq_map_out_expected == freq_map_out_calculated

    def test__build_sum_of_digits_list(self) -> None:
        soln: Solution = Solution()
        sum_of_digits_list_out_expected: List[int]
        sum_of_digits_list_out_calculated: List[int]

        sum_of_digits_list_out_calculated = soln._build_sum_of_digits_list(low=0, high=0)
        sum_of_digits_list_out_expected = [0]
        assert sum_of_digits_list_out_expected == sum_of_digits_list_out_calculated

        sum_of_digits_list_out_calculated = soln._build_sum_of_digits_list(low=1, high=10)
        sum_of_digits_list_out_expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        assert sum_of_digits_list_out_expected == sum_of_digits_list_out_calculated

        sum_of_digits_list_out_calculated = soln._build_sum_of_digits_list(low=13, high=31)
        sum_of_digits_list_out_expected = [4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 3, 4]
        assert sum_of_digits_list_out_expected == sum_of_digits_list_out_calculated

    def test_build_sum_of_digits_dict(self) -> None:
        soln: Solution = Solution()
        sum_of_digits_dict_out_expected: Dict[int, int]
        sum_of_digits_dict_out_calculated: Dict[int, int]

        sum_of_digits_dict_out_calculated = soln._build_sum_of_digits_dict(low=0, high=0)
        sum_of_digits_dict_out_expected = {0: 1}
        assert sum_of_digits_dict_out_expected == sum_of_digits_dict_out_calculated

        sum_of_digits_dict_out_calculated = soln._build_sum_of_digits_dict(low=1, high=10)
        sum_of_digits_dict_out_expected = {
            1: 2,
            2: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 1,
            9: 1
        }
        assert sum_of_digits_dict_out_expected == sum_of_digits_dict_out_calculated

        sum_of_digits_dict_out_calculated = soln._build_sum_of_digits_dict(low=13, high=31)
        sum_of_digits_dict_out_expected = {
            2: 1,
            3: 2,
            4: 3,
            5: 2,
            6: 2,
            7: 2,
            8: 2,
            9: 2,
            10: 2,
            11: 1
        }
        assert sum_of_digits_dict_out_expected == sum_of_digits_dict_out_calculated

    def test_calculate_max_freq(self) -> None:
        soln: Solution = Solution()
        freq_map: Dict[int, int]
        max_freq_out_expected: int
        max_freq_out_calculated: int

        freq_map = {}
        max_freq_out_expected = 0
        max_freq_out_calculated = soln._calculate_max_freq(freq_map=freq_map)
        assert max_freq_out_expected == max_freq_out_calculated

        freq_map = {1: 1}
        max_freq_out_expected = 1
        max_freq_out_calculated = soln._calculate_max_freq(freq_map=freq_map)
        assert max_freq_out_expected == max_freq_out_calculated

        freq_map = {
            -45: 8,
            64: 1,
            0: 3,
            -9: 7,
            34: 4,
            12: 7,
            -21: 2,
            56: 8
        }
        max_freq_out_expected = 8
        max_freq_out_calculated = soln._calculate_max_freq(freq_map=freq_map)
        assert max_freq_out_expected == max_freq_out_calculated

        freq_map = {
            -45: 8,
            64: 19,
            0: 3,
            -9: 7,
            34: 4,
            12: 7,
            -21: 2,
            56: 8
        }
        max_freq_out_expected = 19
        max_freq_out_calculated = soln._calculate_max_freq(freq_map=freq_map)
        assert max_freq_out_expected == max_freq_out_calculated

        freq_map = {
            -45: 8,
            64: 1,
            0: 3,
            -9: 7,
            34: 4,
            12: 7,
            -21: 2,
            56: 8,
            14: 9
        }
        max_freq_out_expected = 9
        max_freq_out_calculated = soln._calculate_max_freq(freq_map=freq_map)
        assert max_freq_out_expected == max_freq_out_calculated

    def test_count_items_with_freq(self) -> None:
        soln: Solution = Solution()
        freq_map: Dict[int, int]
        freq: int
        num_items_with_freq_out_expected: int
        num_items_with_freq_out_calculated: int

        freq_map = {}
        freq = 0
        num_items_with_freq_out_expected = 0
        num_items_with_freq_out_calculated = soln._count_items_with_freq(freq_map=freq_map, freq=freq)
        assert num_items_with_freq_out_expected == num_items_with_freq_out_calculated

        freq_map = {1: 1}

        freq = 1
        num_items_with_freq_out_expected = 1
        num_items_with_freq_out_calculated = soln._count_items_with_freq(freq_map=freq_map, freq=freq)
        assert num_items_with_freq_out_expected == num_items_with_freq_out_calculated

        freq = 3
        num_items_with_freq_out_expected = 0
        num_items_with_freq_out_calculated = soln._count_items_with_freq(freq_map=freq_map, freq=freq)
        assert num_items_with_freq_out_expected == num_items_with_freq_out_calculated

        freq_map = {
            -45: 8,
            64: 19,
            0: 3,
            -9: 7,
            34: 4,
            12: 7,
            -21: 2,
            56: 8
        }

        freq = 6
        num_items_with_freq_out_expected = 0
        num_items_with_freq_out_calculated = soln._count_items_with_freq(freq_map=freq_map, freq=freq)
        assert num_items_with_freq_out_expected == num_items_with_freq_out_calculated

        freq = 7
        num_items_with_freq_out_expected = 2
        num_items_with_freq_out_calculated = soln._count_items_with_freq(freq_map=freq_map, freq=freq)
        assert num_items_with_freq_out_expected == num_items_with_freq_out_calculated

        freq = 4
        num_items_with_freq_out_expected = 1
        num_items_with_freq_out_calculated = soln._count_items_with_freq(freq_map=freq_map, freq=freq)
        assert num_items_with_freq_out_expected == num_items_with_freq_out_calculated

    def test_countLargestGroup(self) -> None:
        soln: Solution = Solution()
        n: int
        num_largest_group_out_expected: int
        num_largest_group_out_calculated: int

        n = 13
        num_largest_group_out_expected = 4
        num_largest_group_out_calculated = soln.countLargestGroup(n=n)
        assert num_largest_group_out_expected == num_largest_group_out_calculated

        n = 2
        num_largest_group_out_expected = 2
        num_largest_group_out_calculated = soln.countLargestGroup(n=n)
        assert num_largest_group_out_expected == num_largest_group_out_calculated

        n = 15
        num_largest_group_out_expected = 6
        num_largest_group_out_calculated = soln.countLargestGroup(n=n)
        assert num_largest_group_out_expected == num_largest_group_out_calculated

        n = 24
        num_largest_group_out_expected = 5
        num_largest_group_out_calculated = soln.countLargestGroup(n=n)
        assert num_largest_group_out_expected == num_largest_group_out_calculated


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()

    soln_test.test_calculate_sum_of_digits()
    soln_test.test_build_freq_map()
    soln_test.test__build_sum_of_digits_list()
    soln_test.test_build_sum_of_digits_dict()
    soln_test.test_calculate_max_freq()
    soln_test.test_count_items_with_freq()
    soln_test.test_countLargestGroup()
