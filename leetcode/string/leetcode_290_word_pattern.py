# leetcode_290https://leetcode.com/problems/word-pattern/description/?envType=problem-list-v2&envId=string
from os.path import split
from typing import List, Dict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #split string into words
        words = s.split(" ")

        #check if length match
        if len(pattern) != len(words):
            return False

        #create two dictionaries for bidirectional mapping
        char_to_word = {}
        word_to_char = {}

        # #check pattern matching-1
        # for char, word in zip(pattern, words):
        #     #if char exists in mapping
        #     if char in char_to_word:
        #         if char_to_word[char] != word:
        #             return False
        #     #if word exists in mapping:
        #     elif word in word_to_char:
        #         if word_to_char[word] != char:
        #             return False
        #     else:
        #         char_to_word[char] = word
        #         word_to_char[word] = char
        # return True

        # check pattern matching-2
        for char, word in zip(pattern, words):
            if char in char_to_word and char_to_word[char] != word:
                return False
            if word in word_to_char and word_to_char[word] != char:
                return False
            char_to_word[char] = word
            word_to_char[word] = char

        return True


    def wordPattern1(self, pattern: str, s: str) -> bool:
        # split string into words
        words = s.split()

        # check if length match
        if len(pattern) != len(words):
            return False

        return (len(set(pattern))) == len(set(words)) == len(set(zip(pattern, words)))


class SolutionTest:
    def test_wordPattern(self) -> None:
        soln: Solution = Solution()
        assert soln.wordPattern(pattern = "abba", s = "dog cat cat dog") == True
        assert soln.wordPattern(pattern = "abba", s = "dog cat cat fish") == False


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_wordPattern()