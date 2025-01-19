#leetcode_3136:-https://leetcode.com/problems/valid-word
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel: bool = False
        has_consonant: bool = False

        for ch in word:
            if not ch.isalnum():
                return False

            if ch.isalpha():
                if self.is_vowel(ch):
                    has_vowel: bool = True
                else:
                    has_consonant: bool = True

        return has_vowel and has_consonant


    def is_vowel(self, ch: str) -> bool:
        vowels = {'a','e','i','o','u'}
        return ch.lower() in vowels

class SolutionTest:
    def test_isValid(self):
        solution = Solution()
        assert solution.isValid("234Adas") == True
        assert solution.isValid("a3$e") == False

if __name__ == '__main__':
    solution_test: SolutionTest = SolutionTest()
    solution_test.test_isValid()



