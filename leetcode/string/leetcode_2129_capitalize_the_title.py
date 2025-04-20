# leetcode_2129_https://leetcode.com/problems/capitalize-the-title

class Solution:
    def capitalizeTitle(self, title: str) -> str:
         words = title.split()
         for i in range(len(words)):
             if len(words[i]) <= 2:
                 words[i] = words[i].lower()
             else:
                 words[i] = words[i].capitalize()
         return ' '.join(words)

class SolutionTest:
    def check_capitalizeTitle(self) -> None:
        soln: Solution = Solution()
        assert soln.capitalizeTitle(title = "capiTalIze tHe titLe") == "Capitalize The Title"
        assert soln.capitalizeTitle(title = "First leTTeR of EACH Word") == "First Letter of Each Word"

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_capitalizeTitle()










