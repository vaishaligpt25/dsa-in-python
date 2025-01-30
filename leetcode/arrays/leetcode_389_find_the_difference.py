#leetcode_389:-https://leetcode.com/problems/find-the-difference/

from typing import List, Dict, Set
from collections import Counter


class Solution:
    def findTheDifference1(self, s: str, t: str) -> str:
        #create frequency counters for both strings
        s_count = Counter(s)
        t_count = Counter(t)

        # find the character with different frequency
        for char in t:
            if char not in s_count or t_count[char] > s_count[char]:
                return char
        return ' '

    def findTheDifference2(self, s: str, t: str) -> str:
        s_count, t_count = Counter(s), Counter(t)

        for char in t_count:
            if char not in s_count:
                return char
            if s_count[char] < t_count[char]:
                return char
        #return ' '


class SolutionTest:
    def difference_is(self) -> None:
        soln: Solution = Solution()
        assert soln.findTheDifference2(s="abcd", t="abcde") == 'e'
        assert soln.findTheDifference2(s=" ", t="y") == 'y'


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.difference_is()



