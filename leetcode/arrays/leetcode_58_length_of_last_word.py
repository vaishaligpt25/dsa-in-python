# # leetcode_58:-https://leetcode.com/problems/length-of-last-word/description/?envType=problem-list-v2&envId=string

from typing import List, Set


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # trim trailing spaces and split into words
        length = 0
        # start from the end of string
        i = len(s) - 1

        # skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        #count characters in last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length


class SolutionTest:
    def test_lengthOfLastWord(self) -> None:
        soln: Solution = Solution()
        assert soln.lengthOfLastWord(s="Hello World") == 5
        assert soln.lengthOfLastWord(s="vaishali") == 8
        assert soln.lengthOfLastWord(s="") == 0

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_lengthOfLastWord()



