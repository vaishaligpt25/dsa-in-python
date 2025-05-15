# leetcode_387: https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq: dict[str, int] = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        for i, char in enumerate(s):
            if char_freq[char] == 1:
                return i

        return -1


class SolutionTest:
    def check_firstUniqChar(self) -> None:
        soln: Solution = Solution()
        assert soln.firstUniqChar(s="leetcode") == 0
        assert soln.firstUniqChar(s="loveleetcode") == 2


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_firstUniqChar()
