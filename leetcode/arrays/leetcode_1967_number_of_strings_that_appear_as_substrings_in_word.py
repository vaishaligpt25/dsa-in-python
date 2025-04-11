# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word

from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count

    def numOfStrings1(self, patterns: List[str], word: str) -> int:
        return sum(1 for pattern in patterns if pattern in word)


class SolutionTest:
    def check_numOfStrings(self) -> None:
        soln: Solution = Solution()
        assert soln.numOfStrings(patterns = ["a","abc","bc","d"], word = "abc") == 3
        assert soln.numOfStrings(patterns = ["a","b","c"], word = "aaaaabbbbb") == 2

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_numOfStrings()