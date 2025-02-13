# https://leetcode.com/problems/sort-the-students-by-their-kth-score

from typing import List, Tuple


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # one-liner
        # return sorted(score, key= lambda x: x[k], reverse=True)

        # Using sort method
        # score.sort(key=lambda x: x[k], reverse=True)
        # return score

        # create pairs of (row, k-th score)
        pairs = [(row, row[k]) for row in score]

        # sort by k-th score
        sorted_pairs = sorted(pairs, key = lambda x : x[1], reverse= True)

        # extract row in sorted pair
        return [pair[0] for pair in sorted_pairs]

