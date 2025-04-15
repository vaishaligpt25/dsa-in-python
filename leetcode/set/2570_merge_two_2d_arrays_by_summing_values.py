# leetcode_2570:https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values
from typing import List, Dict
from collections import Counter


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        id_value: dict[int, int] = {}
        for id, value in nums1:
            id_value[id] = id_value.get(id, 0) + value
        for id, value in nums2:
            id_value[id] = id_value.get(id, 0) + value

        return sorted([[id, value] for id, value in id_value.items()])


    def mergeArrays1(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        counter = Counter()
        for id, value in nums1 + nums2:
            counter[id] += value
        return sorted([id, value] for id, value in counter.items())



