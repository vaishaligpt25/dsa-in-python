# leetcode_2315_https://leetcode.com/problems/count-asterisks/description

class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        inside_pair = False

        for char in s:
            if char == '|':
                inside_pair = not inside_pair
            elif char == '*' and not inside_pair:
                count += 1

        return count

class SolutionTest:
    def teat_counterAsterisks(self) -> None:
        soln: Solution = Solution()
        assert soln.countAsterisks(s = "l|*e*et|c**o|*de|") == 2
        assert soln.countAsterisks(s = "iamprogrammer") == 0
        assert soln.countAsterisks(s = "yo|uar|e**|b|e***au|tifu|l") == 5

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.teat_counterAsterisks()



