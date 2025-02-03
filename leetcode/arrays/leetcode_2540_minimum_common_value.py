#leetcode_2540:-https://leetcode.com/problems/minimum-common-value

from typing import List, Set, Dict

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        return min((num for num in nums2 if num in set1), default = -1)

