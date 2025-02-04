# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences
from itertools import count
from typing import List, Dict, Set
from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = Counter(s)
        # get the count of first character as reference
        target = counts[s[0]]
        # check if all characters have the same count
        return all(count == target for count in counts.values())


def areOccurrencesEqual1(self, s: str) -> bool:
    # count frequency using dictionary
    counts: Dict[str, int] = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    # get all frequency values and check if they are all the same
    frequencies: Set[int] = set(counts.values())
    return len(frequencies) == 1


def areOccurrencesEqual2(self, s: str) -> bool:
    return len(set(Counter(s).values())) == 1


class SolutionTest:
    def check_occurence(self) -> None:
        soln: Solution = Solution()
        assert soln.areOccurrencesEqual(s="abacbc") == True
        assert soln.areOccurrencesEqual(s="aaabb") == False


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_occurence()
