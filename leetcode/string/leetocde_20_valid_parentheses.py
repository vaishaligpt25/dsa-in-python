# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            previous_length = len(s)

            s =s.replace('()', '')
            s =s.replace('[]', '')
            s =s.replace('{}', '')

            if previous_length == len(s):
                return False

        return True


class SolutionTest:
    def test_isValid(self) -> None:
        soln: Solution = Solution()
        assert soln.isValid( s = "()") == True
        assert soln.isValid("()[]{") == False


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_isValid()

