# https://leetcode.com/problems/kth-distinct-string-in-an-array
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        # count frequency of each string
        for s in arr:
            freq[s] = freq.get(s, 0) + 1
        # Count distinct strings in order of appearance
        distinct_count = 0
        for s in arr:
            if freq[s] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return s
        return ""




