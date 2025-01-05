# leetcode-1090:-https://leetcode.com/problems/largest-values-from-labels

from typing import List, Dict, Tuple


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        zipped_list: List[Tuple[int, int]] = self._create_zipped_list_1b(values=values, labels=labels)
        zipped_list_sorted_by_values: List[Tuple[int, int]] = self._create_sorted_zipped_list(zipped_list=zipped_list)
        return self._calculate_max_sum(
            value_labels=zipped_list_sorted_by_values,
            num_values_to_pick=numWanted,
            per_label_max_allowed_frequency=useLimit)


    def _create_zipped_list_1a(self, values: List[int], labels: List[int]) -> List[Tuple[int, int]]:
        if len(values) != len(labels):
            raise ValueError("Dissimilar length inputs")

        zipped_list: List[Tuple[int, int]] = [(-1, -1)] * len(values)
        for i in range(0, len(values)):
            zipped_list[i]: Tuple[int, int] = values[i], labels[i]
        return zipped_list

    def _create_zipped_list_1b(self, values: List[int], labels: List[int]) -> List[Tuple[int, int]]:
        zipped_list: List[Tuple[int, int]] = []
        for i in range(0, len(values)):
            zipped_list.append((values[i], labels[i]))
        return zipped_list

    def _create_zipped_list_2(self, values: List[int], labels: List[int]) -> List[Tuple[int, int]]:
        return list(zip(values, labels))

    def _create_sorted_zipped_list(self, zipped_list: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        return sorted(zipped_list, reverse=True)

    def _calculate_max_sum(

            self,
            value_labels: List[Tuple[int, int]],
            num_values_to_pick: int,
            per_label_max_allowed_frequency: int) -> int:
        sum: int = 0
        num_values_picked: int = 0
        label_frequencies: Dict[int, int] = {}

        for value, label in value_labels:
            crr_label_frequency: int = label_frequencies.get(label, 0)
            if crr_label_frequency >= per_label_max_allowed_frequency:
                continue

            sum: int = sum + value
            num_values_picked: int = num_values_picked + 1
            label_frequencies[label]: int = crr_label_frequency + 1

            if num_values_picked >= num_values_to_pick:
                break

        return sum



class SolutionTest:
    def test__create_zipped_list_1(self) -> None:
        soln: Solution = Solution()
        values_in: List[int]
        labels_in: List[int]
        result_out_expected: List[Tuple[int, int]]
        result_out_computed: List[Tuple[int, int]]

        values_in = [5, 4, 3, 2, 1]
        labels_in = [1, 1, 2, 2, 3]
        result_out_expected = [(5, 1), (4, 1), (3, 2), (2, 2), (1, 3)]

        result_out_computed = soln._create_zipped_list_1a(values=values_in, labels=labels_in)
        assert result_out_expected == result_out_computed

        result_out_computed = soln._create_zipped_list_1b(values=values_in, labels=labels_in)
        assert result_out_expected == result_out_computed

        result_out_computed = soln._create_zipped_list_2(values=values_in, labels=labels_in)
        assert result_out_expected == result_out_computed

        values_in = []
        labels_in = []
        result_out_expected = []

        result_out_computed = soln._create_zipped_list_1a(values=values_in, labels=labels_in)
        assert result_out_expected == result_out_computed

        result_out_computed = soln._create_zipped_list_1b(values=values_in, labels=labels_in)
        assert result_out_expected == result_out_computed

        result_out_computed = soln._create_zipped_list_2(values=values_in, labels=labels_in)
        assert result_out_expected == result_out_computed

        values_in = [5]
        labels_in = [2]
        result_out_expected = [(5, 2)]

        result_out_computed = soln._create_zipped_list_1a(values=values_in, labels=labels_in)
        assert result_out_expected == result_out_computed

        result_out_computed = soln._create_zipped_list_1b(values=values_in, labels=labels_in)
        assert result_out_expected == result_out_computed

        result_out_computed = soln._create_zipped_list_2(values=values_in, labels=labels_in)
        assert result_out_expected == result_out_computed

    def test__create_sorted_zipped_list(self) -> None:
        soln: Solution = Solution()
        zipped_list_in: List[Tuple[int, int]]
        result_out_expected: List[Tuple[int, int]]
        result_out_computed: List[Tuple[int, int]]

        zipped_list_in = [(3, 1), (5, 2), (7, 2)]
        result_out_expected = [(7, 2), (5, 2), (3, 1)]
        result_out_computed = soln._create_sorted_zipped_list(zipped_list=zipped_list_in)
        assert result_out_expected == result_out_computed

    def test__calculate_max_sum(self) -> None:
        soln: Solution = Solution()
        value_labels: List[Tuple[int, int]]
        num_values_to_pick: int
        per_label_max_allowed_frequency: int
        max_sum_out_expected: int
        max_sum_out_computed: int

        value_labels = [(5, 1), (4, 1), (3, 2), (2, 2), (1, 3)]
        num_values_to_pick = 3
        per_label_max_allowed_frequency = 1
        max_sum_out_expected = 9
        max_sum_out_computed = soln._calculate_max_sum(
            value_labels=value_labels,
            num_values_to_pick=num_values_to_pick,
            per_label_max_allowed_frequency=per_label_max_allowed_frequency)
        assert max_sum_out_expected == max_sum_out_computed

        value_labels = [(5, 1), (4, 3), (3, 3), (2, 3), (1, 2)]
        num_values_to_pick = 3
        per_label_max_allowed_frequency = 2
        max_sum_out_expected = 12
        max_sum_out_computed = soln._calculate_max_sum(
            value_labels=value_labels,
            num_values_to_pick=num_values_to_pick,
            per_label_max_allowed_frequency=per_label_max_allowed_frequency)
        assert max_sum_out_expected == max_sum_out_computed

        value_labels = [(9, 0), (8, 0), (8, 0), (7, 1), (6, 1)]
        num_values_to_pick = 3
        per_label_max_allowed_frequency = 1
        max_sum_out_expected = 16
        max_sum_out_computed = soln._calculate_max_sum(
            value_labels=value_labels,
            num_values_to_pick=num_values_to_pick,
            per_label_max_allowed_frequency=per_label_max_allowed_frequency)
        assert max_sum_out_expected == max_sum_out_computed


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()

    soln_test.test__create_zipped_list_1()
    soln_test.test__create_sorted_zipped_list()
    soln_test.test__calculate_max_sum()
