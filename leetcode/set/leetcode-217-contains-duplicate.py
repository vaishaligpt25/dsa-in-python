from typing import List, Dict, Set, Optional


class Solution:
    # ------ method-1: sorting ------

    def _contains_duplicate_1a_sorting_1(self, nums: List[int]) -> bool:
        nums_sorted: List[int] = sorted(nums)
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i - 1] == nums_sorted[i]:
                return True
        return False

    def _contains_duplicate_1b_sorting_2(self, nums: List[int]) -> bool:
        nums_sorted: List[int] = sorted(nums)
        prev_val = None
        for curr_val in nums_sorted:
            if prev_val == curr_val:
                return True
            prev_val = curr_val
        return False

    # ------ method-2: dictionary ------

    def _contains_duplicate_2_dictionary(self, nums: List[int]) -> bool:
        my_dict: Dict[int, bool] = {}
        for num in nums:
            # check if we've already seen num before
            if num in my_dict:
                return True
            # add num in dictionary for checking in future
            my_dict[num]: bool = True
        return False

    # ------ method-3: set ------

    def _contains_duplicate_3_set(self, nums: List[int]) -> bool:
        my_set: Set[int] = set()
        for num in nums:
            # check if we've already seen num before
            if num in my_set:
                return True
            # add num in set for checking in future
            my_set.add(num)
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        return self._contains_duplicate_3_set(nums=nums)


class SolutionTest:
    def test_containsDuplicate(self) -> None:
        soln: Solution = Solution()

        assert soln.containsDuplicate(nums=[1, 2, 3, 4, 1]) == True
        assert soln.containsDuplicate(nums=[1, 2, 3, 4]) == False
        assert soln.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
        assert soln.containsDuplicate(nums=[1]) == False
        assert soln.containsDuplicate(nums=[]) == False


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_containsDuplicate()
