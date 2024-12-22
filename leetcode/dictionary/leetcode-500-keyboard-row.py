# LeetCode-500: https://leetcode.com/problems/keyboard-row

from typing import List, Dict, Set


class Solution:
    def find_words_method_1(self, words: List[str]) -> List[str]:
        words_that_can_be_formed_by_single_row: List[str] = []
        for word in words:
            if self._soln_method_1(word=word.lower()):
                words_that_can_be_formed_by_single_row.append(word)
        return words_that_can_be_formed_by_single_row

    def find_words_method_2(self, words: List[str]) -> List[str]:
        return [word for word in words if self._soln_method_4(word=word.lower())]

    def findWords(self, words: List[str]) -> List[str]:
        return self.find_words_method_2(words=words)

    # ------- method-1 -------

    ROW_1_LIST: List[str] = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    ROW_2_LIST: List[str] = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    ROW_3_LIST: List[str] = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

    def _can_form_word_with_alphabets_1(self, word: str, alphabets: List[str]) -> bool:
        for character in word:
            if character not in alphabets:
                return False
        return True

    def _soln_method_1(self, word: str) -> bool:
        return self._can_form_word_with_alphabets_1(word=word, alphabets=Solution.ROW_1_LIST) \
            or self._can_form_word_with_alphabets_1(word=word, alphabets=Solution.ROW_2_LIST) \
            or self._can_form_word_with_alphabets_1(word=word, alphabets=Solution.ROW_3_LIST)

    def _soln_method_1_1(self, word: str) -> bool:
        ALPHABET_ROWS: List[List[str]] = [
            Solution.ROW_1_LIST,
            Solution.ROW_2_LIST,
            Solution.ROW_3_LIST
        ]

        for alphabet_row in ALPHABET_ROWS:
            if self._can_form_word_with_alphabets_1(word=word, alphabets=alphabet_row):
                return True
        return False

    # ------- method-2 -------

    ROW_1_SET: Set[str] = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    ROW_2_SET: Set[str] = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
    ROW_3_SET: Set[str] = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

    def _can_form_word_with_alphabets_2(self, word: str, alphabets: Set[str]) -> bool:
        for character in word:
            if character not in alphabets:
                return False
        return True

    def _soln_method_2(self, word: str) -> bool:
        return self._can_form_word_with_alphabets_2(word=word, alphabets=Solution.ROW_1_SET) \
            or self._can_form_word_with_alphabets_2(word=word, alphabets=Solution.ROW_2_SET) \
            or self._can_form_word_with_alphabets_2(word=word, alphabets=Solution.ROW_3_SET)

    # ------- method-3 -------

    ROWS_DICT_USING_LIST: Dict[int, List[str]] = {
        0: ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        1: ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        2: ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    }

    def _soln_method_3(self, word: str) -> bool:
        for alphabet_row in Solution.ROWS_DICT_USING_LIST.values():
            if self._can_form_word_with_alphabets_1(word=word, alphabets=alphabet_row):
                return True
        return False

    # ------- method-4 -------

    ALPHABET_ROW_DICT: Dict[str, int] = {
        "a": 1,
        "b": 2,
        "c": 2,
        "d": 1,
        "e": 0,
        "f": 1,
        "g": 1,
        "h": 1,
        "i": 0,
        "j": 1,
        "k": 1,
        "l": 1,
        "m": 2,
        "n": 2,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 1,
        "t": 0,
        "u": 0,
        "v": 2,
        "w": 0,
        "x": 2,
        "y": 0,
        "z": 2
    }

    def _soln_method_4(self, word: str) -> bool:
        # if len(word) <= 1:
        #     return True

        # "v", "a", "i" ..
        first_character_row: int = Solution.ALPHABET_ROW_DICT.get(word[0])
        for character in word[1:]:
            character_row: int = Solution.ALPHABET_ROW_DICT.get(character)
            if character_row != first_character_row:
                return False
        return True

class SolutionTest:
    def test__soln_method_1(self) -> None:
        soln: Solution = Solution()

        assert soln._soln_method_1(word="vaishali") == False
        assert soln._soln_method_1(word="pot") == True
        assert soln._soln_method_1(word="qwpri") == True
        assert soln._soln_method_1(word="alkfh") == True
        assert soln._soln_method_1(word="mcnz") == True
        assert soln._soln_method_1(word="cow") == False

    def test__soln_method_2(self) -> None:
        soln: Solution = Solution()

        assert soln._soln_method_2(word="vaishali") == False
        assert soln._soln_method_2(word="pot") == True
        assert soln._soln_method_2(word="qwpri") == True
        assert soln._soln_method_2(word="alkfh") == True
        assert soln._soln_method_2(word="mcnz") == True
        assert soln._soln_method_2(word="cow") == False

    def test__soln_method_4(self) -> None:
        soln: Solution = Solution()

        assert soln._soln_method_4(word="vaishali") == False
        assert soln._soln_method_4(word="pot") == True
        assert soln._soln_method_4(word="qwpri") == True
        assert soln._soln_method_4(word="alkfh") == True
        assert soln._soln_method_4(word="mcnz") == True
        assert soln._soln_method_4(word="cow") == False
        assert soln._soln_method_4(word="i") == True

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()

    soln_test.test__soln_method_1()
    soln_test.test__soln_method_2()
    soln_test.test__soln_method_4()
