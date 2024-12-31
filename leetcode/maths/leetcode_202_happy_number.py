#leetcode-202: https://leetcode.com/problems/happy-number

from math import trunc
from typing import List, Set

class Solution:
    # ------- calculate sum of squares of digits: method-1 ---------

    def _get_sum_of_values(self, my_list: List[int]) -> int:
        # sum: int = 0
        # for val in my_list:
        #     sum: int = sum + val
        # return sum
        return sum(my_list)

    def _get_squares_of_values(self, my_list: List[int]) -> List[int]:
        return list(map(lambda val: val * val, my_list))
        # return [(val * val) for val in my_list]

    def _get_digits(self, num: int) -> List[int]:
        # return list(map(int, str(num)))
        # return list(map(lambda digit: int(digit), str(num)))
        return [int(digit) for digit in str(num)]

    def _get_sum_of_squares_of_digit_1(self, num: int) -> int:
        digits: List[int] = self._get_digits(num=num)
        digit_squares: List[int] = self._get_squares_of_values(my_list=digits)
        sum_of_squares_of_digits: int = self._get_sum_of_values(my_list=digit_squares)
        return sum_of_squares_of_digits

    # ------- calculate sum of squares of digits: method-2 (same but condensed) ---------

    def _get_sum_of_squares_of_digit_2(self, num: int) -> int:
        return sum([int(digit) * int(digit) for digit in str(num)])

    ####################################################

    # ------ repeat process: method-1 (iteration) -------

    def _is_happy_1_iterative(self, num: int) -> bool:
        numbers_already_seen: Set[int] = set()
        while num != 1:
            # check if we have seen this number before
            if num in numbers_already_seen:
                return False

            # add number to set indicating that we've seen it before
            numbers_already_seen.add(num)

            # transform number: replace with sum of square of digits
            num: int = self._get_sum_of_squares_of_digit_1(num=num)
        return True

    # ------ repeat process: method-2 (recursion) -------

    def _is_happy_2_recursion(self, num: int, numbers_already_seen: Set[int]) -> bool:
        if num == 1:
            return True
        elif num in numbers_already_seen:
            return False
        else:
            numbers_already_seen.add(num)

            num: int = self._get_sum_of_squares_of_digit_1(num=num)
            return self._is_happy_2_recursion(num=num, numbers_already_seen=numbers_already_seen)

    #####################################################

    def isHappy(self, n: int) -> bool:
        return self._is_happy_2_recursion(num=n, numbers_already_seen=set())
        # return self._is_happy_1_iterative(num=n)


class SolutionTest:
    def test_isHappy(self) -> None:
        soln: Solution = Solution()
        assert soln.isHappy(n=19) == True
        assert soln.isHappy(n=2) == False
        assert soln.isHappy(n=7) == True

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_isHappy()
