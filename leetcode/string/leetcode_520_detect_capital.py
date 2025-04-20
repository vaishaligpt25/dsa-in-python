# leetcode_520_https://leetcode.com/problems/detect-capital/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        if word.islower():
            return True
        if word[0].isupper()and word[1:].islower():
            return True
        return False

class SolutionTest:
    def check_detectCapitalUse(self) -> None:
        soln: Solution = Solution()
        assert soln.detectCapitalUse(word = "USA") == True
        assert soln.detectCapitalUse(word= "FlaG") == False

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_detectCapitalUse()


