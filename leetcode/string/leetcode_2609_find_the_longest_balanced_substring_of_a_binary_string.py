# leetcode_2609:-https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_length = 0
        i = 0

        while i < len(s):
           #count consecutive zeroes:
           zeroes = 0
           while i < len(s) and s[i] == '0':
               zeroes += 1
               i += 1

           # count consecutive ones
           ones = 0
           while i < len(s) and s[i] == '1':
               ones += 1
               i += 1

           # balanced substring length is min (zeroes,ones) * 2
           max_length = max(max_length, min(zeroes,ones) * 2)

        return max_length

class SolutionTest:
    def test_findTheLongestBalancedSubstring(self) -> None:;
    soln = Solution()

    assert soln.findTheLongestBalancedSubstring("01000111") == 6
    assert soln.findTheLongestBalancedSubstring("00111") == 4
    assert soln.findTheLongestBalancedSubstring("111") == 0

if __name__ == '__main__':
    soln_test = SolutionTest()
    soln_test.test_findTheLongestBalancedSubstring()