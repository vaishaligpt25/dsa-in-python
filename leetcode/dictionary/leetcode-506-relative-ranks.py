# LeetCode-506: https://leetcode.com/problems/relative-ranks/

from typing import List, Dict


class Solution:
    TOP_RANK_TITLES: List[str] = [
        "Gold Medal",
        "Silver Medal",
        "Bronze Medal"
    ]

    def _create_dict_with_index_as_value(self, my_list: List[int]) -> Dict[int, int]:
        my_dict: Dict[int, int] = {}
        for i in range(0, len(my_list)):
            my_dict[my_list[i]]: int = i + 1
        return my_dict

    def _get_rank_str(self, rank: int) -> str:
        if rank <= 3:
            return Solution.TOP_RANK_TITLES[rank - 1]
        else:
            return str(rank)

    def _build_ranks_list(self, scores: List[int], scores_with_ranks: Dict[int, int]) -> List[str]:
        return [self._get_rank_str(rank=scores_with_ranks[score]) for score in scores]

    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        if not scores:
            return []
        if len(scores) == 1:
            return [Solution.TOP_RANK_TITLES[0]]

        sorted_scores: List[int] = sorted(scores, reverse=True)
        scores_with_ranks: Dict[int, int] = self._create_dict_with_index_as_value(my_list=sorted_scores)
        return self._build_ranks_list(scores=scores, scores_with_ranks=scores_with_ranks)

class SolutionTest:
    def test_relative_ranks(self) -> None:
        soln : Solution = Solution()

        assert soln.findRelativeRanks(scores= [10,3,8,9,4])== ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
        assert soln.findRelativeRanks(scores= [5,4,3,2,1])== ["Gold Medal","Silver Medal","Bronze Medal","4","5"]


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_relative_ranks()
