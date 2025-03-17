# https://leetcode.com/problems/two-out-of-three

from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # Convert lists to sets for efficient lookup
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        # Find numbers that appear in at least two sets
        result = set()

        # Check numbers in set1
        for num in set1:
            if num in set2 or num in set3:
                result.add(num)

        # Check numbers in set2
        for num in set2:
            if num in set3:
                result.add(num)

        return list(result)
