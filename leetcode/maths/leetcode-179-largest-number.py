# LeetCode-179: https://leetcode.com/problems/largest-number/

# tricky problem: referenced from Editorial on LeetCode

from typing import List


class Solution:
    def _is_strictly_prefix(self, prefix: str, prefix_of: str) -> bool:
        return (prefix != prefix_of) and prefix_of.startswith(prefix)

    def _get_first_digit(self, num_str: str) -> int:
        return int(num_str[0])

    def _get_first_digit_after_prefix(self, prefix_num: str, prefix_of_num: str) -> int:
        prefix_of_num_without_prefix: str = prefix_of_num[len(prefix_num):]
        return self._get_first_digit(num_str=prefix_of_num_without_prefix)

    def _is_prefix_and_should_come_before(self, num_that_can_be_prefix: str, num_to_check_prefix_of: str) -> bool:
        if not self._is_strictly_prefix(prefix=num_that_can_be_prefix, prefix_of=num_to_check_prefix_of):
            return False

        # this piece is from Editorial on LeetCode
        return int(num_that_can_be_prefix + num_to_check_prefix_of) > int(num_to_check_prefix_of + num_that_can_be_prefix)

        # first_digit_of_prefix: int = self._get_first_digit(num_str=num_that_can_be_prefix)
        # first_digit_of_prefix_of_after_prefix: int = self._get_first_digit_after_prefix(prefix_num=num_that_can_be_prefix, prefix_of_num=num_to_check_prefix_of)
        # # print(f"_is_prefix_and_should_come_before(num_that_can_be_prefix={num_that_can_be_prefix}, num_to_check_prefix_of={num_to_check_prefix_of}) = (first_digit_of_prefix={first_digit_of_prefix} >= first_digit_of_prefix_of_after_prefix={first_digit_of_prefix_of_after_prefix}) = {first_digit_of_prefix >= first_digit_of_prefix_of_after_prefix}")
        # return first_digit_of_prefix >= first_digit_of_prefix_of_after_prefix

    def _swap_values(self, my_list: List[str], idx_1: int, idx_2: int) -> None:
        tmp: str = my_list[idx_1]
        my_list[idx_1]: str = my_list[idx_2]
        my_list[idx_2]: str = tmp

    def _adjust_nums(self, nums_as_strs: List[str]) -> List[str]:
        adjusted_nums_as_strs: List[str] = nums_as_strs
        for i in range(1, len(adjusted_nums_as_strs)):
            crr_num: str = nums_as_strs[i]

            j: int = i
            while (j >= 1) and self._is_prefix_and_should_come_before(num_that_can_be_prefix=crr_num, num_to_check_prefix_of=nums_as_strs[j - 1]):
                self._swap_values(my_list=adjusted_nums_as_strs, idx_1=j - 1, idx_2=j)
                j: int = j - 1
        return adjusted_nums_as_strs

    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        if len(nums) == 1:
            return str(nums[0])
        if sum(nums) == 0:
            # all input numbers are 0 only
            return "0"

        nums_as_strs: List[str] = list(map(str, nums))

        nums_as_strs_desc: List[str] = sorted(nums_as_strs, reverse=True)
        # print(f"sorted={nums_as_strs_desc}")

        adjusted_nums_as_strs_desc: List[str] = self._adjust_nums(nums_as_strs=nums_as_strs_desc)
        # print(f"adjusted={adjusted_nums_as_strs_desc}")

        return "".join(adjusted_nums_as_strs_desc)


class SolutionTest:
    def test__get_first_digit_after_prefix(self) -> None:
        soln: Solution = Solution()
        prefix_num: str
        prefix_of_num: str

        prefix_num = "31"
        prefix_of_num = "312"
        assert soln._get_first_digit_after_prefix(prefix_num=prefix_num, prefix_of_num=prefix_of_num) == 2

        prefix_num = "3"
        prefix_of_num = "39"
        assert soln._get_first_digit_after_prefix(prefix_num=prefix_num, prefix_of_num=prefix_of_num) == 9

        prefix_num = "3"
        prefix_of_num = "3698"
        assert soln._get_first_digit_after_prefix(prefix_num=prefix_num, prefix_of_num=prefix_of_num) == 6

    def test__is_prefix_and_should_come_before(self) -> None:
        soln: Solution = Solution()
        num_that_can_be_prefix: str
        num_to_check_prefix_of: str

        num_that_can_be_prefix = "31"
        num_to_check_prefix_of = "310"
        assert soln._is_prefix_and_should_come_before(num_that_can_be_prefix=num_that_can_be_prefix, num_to_check_prefix_of=num_to_check_prefix_of) is True

        num_that_can_be_prefix = "31"
        num_to_check_prefix_of = "311"
        assert soln._is_prefix_and_should_come_before(num_that_can_be_prefix=num_that_can_be_prefix, num_to_check_prefix_of=num_to_check_prefix_of) is True

        num_that_can_be_prefix = "31"
        num_to_check_prefix_of = "312"
        assert soln._is_prefix_and_should_come_before(num_that_can_be_prefix=num_that_can_be_prefix, num_to_check_prefix_of=num_to_check_prefix_of) is True

        num_that_can_be_prefix = "31"
        num_to_check_prefix_of = "313"
        assert soln._is_prefix_and_should_come_before(num_that_can_be_prefix=num_that_can_be_prefix, num_to_check_prefix_of=num_to_check_prefix_of) is False

        num_that_can_be_prefix = "31"
        num_to_check_prefix_of = "314"
        assert soln._is_prefix_and_should_come_before(num_that_can_be_prefix=num_that_can_be_prefix, num_to_check_prefix_of=num_to_check_prefix_of) is False

        num_that_can_be_prefix = "31"
        num_to_check_prefix_of = "31"
        assert soln._is_prefix_and_should_come_before(num_that_can_be_prefix=num_that_can_be_prefix, num_to_check_prefix_of=num_to_check_prefix_of) is False

    def test_largestNumber(self) -> None:
        soln: Solution = Solution()
        nums: List[int]

        nums = [10, 2]
        assert soln.largestNumber(nums=nums) == "210"

        nums = [3, 30, 34, 5, 9]
        assert soln.largestNumber(nums=nums) == "9534330"

        nums = [111311, 1113]
        assert soln.largestNumber(nums=nums) == "1113111311"


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()

    soln_test.test__get_first_digit_after_prefix()
    soln_test.test__is_prefix_and_should_come_before()
    soln_test.test_largestNumber()
