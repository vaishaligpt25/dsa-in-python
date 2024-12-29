# LeetCode-219: https://leetcode.com/problems/contains-duplicate-ii

from typing import List, Set, Tuple


class Solution:
    def _build_first_window(self, my_list: List[int], window_size: int) -> Tuple[bool, Set[int]]:
        if len(my_list) <= 1:
            return False, set(my_list)

        my_window_set: Set[int] = set()

        for i in range(0, min(len(my_list), window_size)):
            ele: int = my_list[i]

            if ele in my_window_set:
                return True, my_window_set

            my_window_set.add(ele)

        return False, my_window_set

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k <= 0:
            return False
        if len(nums) <= 1:
            return False

        (first_window_result, my_window_set) = self._build_first_window(my_list=nums, window_size=(k + 1))
        if first_window_result:
            return True

        for i in range(k + 1, len(nums)):
            # remove first element from set
            element_to_remove: int = nums[i - (k + 1)]
            my_window_set.remove(element_to_remove)

            # read k+1th element to be added in window-set
            element_to_add: int = nums[i]
            # check if this element has already occurred in our current window
            if element_to_add in my_window_set:
                return True
            # otherwise add element in window
            my_window_set.add(element_to_add)

        return False


class SolutionTest:
    def test__build_first_window(self) -> None:
        soln: Solution = Solution()
        my_list_in: List[int]
        window_size_in: int
        result_out_expected: Tuple[bool, Set[int]]
        result_out_computed: Tuple[bool, Set[int]]

        my_list_in = list()
        window_size_in = 5
        result_out_expected = (False, set())
        result_out_computed = soln._build_first_window(my_list=my_list_in, window_size=window_size_in)
        assert result_out_expected == result_out_computed

        my_list_in = [8, 1, 3, 7]
        window_size_in = 5
        result_out_expected = (False, {8, 1, 3, 7})
        result_out_computed = soln._build_first_window(my_list=my_list_in, window_size=window_size_in)
        assert result_out_expected == result_out_computed

        my_list_in = [8, 1, 3, 8]
        window_size_in = 5
        result_out_expected = (True, {8, 1, 3})
        result_out_computed = soln._build_first_window(my_list=my_list_in, window_size=window_size_in)
        assert result_out_expected == result_out_computed

        my_list_in = [8, 1, 8, 3]
        window_size_in = 5
        result_out_expected = (True, {8, 1})
        result_out_computed = soln._build_first_window(my_list=my_list_in, window_size=window_size_in)
        assert result_out_expected == result_out_computed

        my_list_in = [8, 1, 8, 3]
        window_size_in = 2
        result_out_expected = (False, {8, 1})
        result_out_computed = soln._build_first_window(my_list=my_list_in, window_size=window_size_in)
        assert result_out_expected == result_out_computed

        my_list_in = [8, 1, 8, 3]
        window_size_in = 3
        result_out_expected = (True, {8, 1})
        result_out_computed = soln._build_first_window(my_list=my_list_in, window_size=window_size_in)
        assert result_out_expected == result_out_computed

        my_list_in = [8, 1, 3, 7]
        window_size_in = 3
        result_out_expected = (False, {8, 1, 3})
        result_out_computed = soln._build_first_window(my_list=my_list_in, window_size=window_size_in)
        assert result_out_expected == result_out_computed

    def test_containsNearbyDuplicate(self) -> None:
        soln: Solution = Solution()
        my_list_in: List[int]
        k_in: int

        my_list_in = []
        k_in = 4
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == False

        my_list_in = [9]
        k_in = 4
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == False

        my_list_in = [8, 1, 3, 7]

        k_in = 2
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == False

        k_in = 3
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == False

        k_in = 4
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == False

        k_in = 5
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == False

        my_list_in = [8, 1, 3, 7, 4, 3, 9, 2, 4]

        k_in = 2
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == False

        k_in = 3
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == True

        k_in = 4
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == True

        k_in = 1234
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == True

        my_list_in = [1, 2, 3, 1]

        k_in = 2
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == False

        k_in = 3
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == True

        my_list_in = [1, 0, 1, 1]

        k_in = 0
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == False

        k_in = 1
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == True

        my_list_in = [1, 2, 3, 1, 2, 3]

        k_in = 0
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == False

        k_in = 1
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == False

        k_in = 2
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == False

        k_in = 3
        assert soln.containsNearbyDuplicate(nums=my_list_in, k=k_in) == True


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()

    soln_test.test__build_first_window()
    soln_test.test_containsNearbyDuplicate()
