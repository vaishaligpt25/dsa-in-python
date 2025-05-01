# leetcode_709_https://leetcode.com/problems/to-lower-case/description

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

    def toLowerCase1(self, s: str) -> str:
        result = ""
        for char in s:
            if 65 <= ord(char) <= 90:
                result += chr(ord(char)+32)
            else:
                result += char
        return result


class SolutionTest:
    def test_toLowerCase(self) -> None:
        soln: Solution = Solution()
        assert soln.toLowerCase(s = "Hello") == "hello"
        assert soln.toLowerCase( s = "here") == "here"

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_toLowerCase()
