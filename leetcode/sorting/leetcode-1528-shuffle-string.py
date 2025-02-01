# LeetCode-1528: https://leetcode.com/problems/shuffle-string/

from typing import List, Tuple


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        if len(s) <= 1:
            return s

        zipped_list: List[Tuple[int, str]] = list(zip(indices, list(s)))
        sorted_zipped_list: List[Tuple[int, str]] = sorted(zipped_list)

        reordered_chars: List[str] = list(map(lambda my_tuple: my_tuple[1], sorted_zipped_list))
        # reordered_chars: List[str] = [my_tuple[1] for my_tuple in sorted_zipped_list]

        return "".join(reordered_chars)
