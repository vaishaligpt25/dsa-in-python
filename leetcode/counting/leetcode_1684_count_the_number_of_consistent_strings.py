#leetcode_1684:-https://leetcode.com/problems/count-the-number-of-consistent-strings

from typing import List, Set, Dict


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set: Set[str] = set(allowed)
        count = 0
        for word in words:
            # Word is consistent if all its characters are in allowed_set
            if all(char in allowed_set for char in word):
                count += 1
        return count


    def countConsistentStrings1(self, allowed: str, words: List[str]) -> int:
        allowed_set: Set[str] = set(allowed)
        return sum(1 for word in words if set(word) <= allowed_set)


class SolutionTest:
    def consistent_string(self) -> None:
        soln: Solution = Solution()
        assert soln.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]) == 2
        assert soln.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]) == 7

        assert soln.countConsistentStrings1(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]) == 2
        assert soln.countConsistentStrings1(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]) == 7


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.consistent_string()

