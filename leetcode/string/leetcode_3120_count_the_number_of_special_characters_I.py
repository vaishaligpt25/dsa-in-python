# leetcode_3120_https://leetcode.com/problems/count-the-number-of-special-characters-i/


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_seen: set[str] = set()
        upper_seen: set[str] = set()

        for char in word:
            if char.islower():
                lower_seen.add(char)
            else:
                upper_seen.add(char.lower())

        count: int = 0
        for char in lower_seen:
            if char in upper_seen:
                count += 1
        return count


class SolutionTest:
    def check_numberOfSpecialChars(self) -> None:
        soln: Solution = Solution()
        assert soln.numberOfSpecialChars(word = "aaAbcBC") == 3
        assert soln.numberOfSpecialChars(word= "AAA") == 0

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_numberOfSpecialChars()

