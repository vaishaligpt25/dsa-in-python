# https://leetcode.com/problems/merge-similar-items
from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        value_weight = {}
        for value, weight in items1:
            value_weight[value] = value_weight.get(value, 0) + weight

        for value, weight in items2:
            value_weight[value] = value_weight.get(value, 0) + weight

        return sorted([[value, weight] for value, weight in value_weight.items()])
