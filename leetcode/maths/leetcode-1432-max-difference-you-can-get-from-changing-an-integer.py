# LeetCode-1432: https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

from typing import List, Set, Tuple


class Solution:
    def _convert_int_to_digit_list(self, num: int) -> List[int]:
        digits = list()
        while num > 0:
            digits.append(num % 10)
            num //= 10
        return digits[::-1]

    def _convert_digit_list_to_int(self, digits: List[int]) -> int:
        num: int = 0
        for i, digit in enumerate(digits[::-1]):
            num += digit * (10 ** i)
        return num

    def _find_most_significant_digit_after_startIdx_that_is_not_in_set(self, digits: List[int], start_idx: int, exclusion_set: Set[int]) -> Tuple[int, int]:
        for idx in range(start_idx, len(digits)):
            digit = digits[idx]
            if digit not in exclusion_set:
                return idx, digit
        return -1, -1

    def _find_most_significant_digit_that_is_not_in_set(self, digits: List[int], exclusion_set: Set[int]) -> Tuple[int, int]:
        return self._find_most_significant_digit_after_startIdx_that_is_not_in_set(digits=digits, start_idx=0, exclusion_set=exclusion_set)

    def _replace_all_occurrences_of_digit_in_list(self, digits: List[int], old_digit: int, new_digit: int) -> List[int]:
        return [new_digit if digit == old_digit else digit for digit in digits]

    def _calculate_max_number_after_replacement(self, digits: List[int]) -> int:
        _, digit_to_replace_with_9 = self._find_most_significant_digit_that_is_not_in_set(digits=digits, exclusion_set={9})
        return self._convert_digit_list_to_int(self._replace_all_occurrences_of_digit_in_list(digits=digits, old_digit=digit_to_replace_with_9, new_digit=9))

    def _calculate_min_number_after_replacement(self, num: int, digits: List[int]) -> int:
        min_number: int
        if digits[0] == 1:
            # first digit is 1, so we would replace first non-1 (and non-0) digit with 0 instead
            _, digit_to_replace_with_0 = self._find_most_significant_digit_after_startIdx_that_is_not_in_set(digits=digits, start_idx=1, exclusion_set={0, 1})
            if digit_to_replace_with_0 == -1:
                # all digits are 1, so num is already min number
                min_number: int = num
            else:
                min_number: int = self._convert_digit_list_to_int(self._replace_all_occurrences_of_digit_in_list(digits=digits, old_digit=digit_to_replace_with_0, new_digit=0))
        else:
            # first digit is NOT 1, so just making it 1 will give us min number
            min_number: int = self._convert_digit_list_to_int(self._replace_all_occurrences_of_digit_in_list(digits=digits, old_digit=digits[0], new_digit=1))
        return min_number

    def maxDiff(self, num: int) -> int:
        digits: List[int] = self._convert_int_to_digit_list(num=num)

        max_number: int = self._calculate_max_number_after_replacement(digits=digits)
        min_number: int = self._calculate_min_number_after_replacement(num=num, digits=digits)

        return max_number - min_number


class SolutionTest:
    def test_maxDiff(self):
        solution = Solution()
        assert solution.maxDiff(555) == 888
        assert solution.maxDiff(9) == 8
        assert solution.maxDiff(123456) == 820000
        assert solution.maxDiff(10000) == 80000
        assert solution.maxDiff(9288) == 8700
        assert solution.maxDiff(1101057) == 8808050


if __name__ == "__main__":
    solution_test: SolutionTest = SolutionTest()
    solution_test.test_maxDiff()
