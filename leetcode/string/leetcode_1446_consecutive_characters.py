# https://leetcode.com/problems/consecutive-characters

class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0

        max_count = 1
        current_count = 1

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 1

        return max_count


class SolutionTest:
    def check_max_power(self) -> None:
        soln: Solution = Solution()
        assert soln.maxPower(s = "leetcode") == 2
        assert soln.maxPower(s = "abbcccddddeeeeedcba") == 5


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_max_power()
