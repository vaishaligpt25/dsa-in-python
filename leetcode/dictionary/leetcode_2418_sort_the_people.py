# https://leetcode.com/problems/sort-the-people

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_dict = dict(zip(heights, names))
        sorted_heights = sorted(heights, reverse=True)
        return [height_dict[h] for h in sorted_heights]

    def sortPeople1(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(heights, names))
        people.sort(reverse=True)
        return [name for _, name in people]

