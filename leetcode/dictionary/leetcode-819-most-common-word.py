# LeetCode-819: https://leetcode.com/problems/most-common-word

import re
from typing import List, Dict, Set, Tuple


class Solution:
    PUNCTUATION_CHARS: str = "[!?',;. ]"

    def _build_frequency_dict_1a(self, my_words: List[str], excluded_words: List[str]) -> Dict[str, int]:
        freq_dict: Dict[str, int] = {}
        for word in my_words:
            if word not in excluded_words:
                freq_dict[word]: int = freq_dict.get(word, 0) + 1
        return freq_dict

    def _build_frequency_dict_1b(self, my_words: List[str], excluded_words: List[str]) -> Dict[str, int]:
        excluded_words_as_set: Set[str] = set(excluded_words)
        freq_dict: Dict[str, int] = {}
        for word in my_words:
            if word not in excluded_words_as_set:
                freq_dict[word]: int = freq_dict.get(word, 0) + 1
        return freq_dict

    def _build_frequency_dict_2a(self, my_words: List[str], excluded_words: List[str]) -> Dict[str, int]:
        freq_dict: Dict[str, int] = {}

        # create dictionary
        for word in my_words:
            freq_dict[word]: int = freq_dict.get(word, 0) + 1

        # method-1: remove banned words from dictionary
        # for word in excluded_words:
        #     freq_dict.pop(word, None)
        # return freq_dict

        # method-2: remove banned words from dictionary
        filtered_freq_dict: Dict[str, int] = {key: value for key, value in freq_dict.items() if key not in excluded_words}
        return filtered_freq_dict

    # advanced (need not learn)
    def _build_frequency_dict_2b_1(self, my_words: List[str], excluded_words: List[str]) -> Dict[str, int]:
        freq_dict: Dict[str, int] = {word: my_words.count(word) for word in set(my_words)}

        # remove banned words from dictionary
        filtered_freq_dict: Dict[str, int] = {key: value for key, value in freq_dict.items() if key not in excluded_words}
        return filtered_freq_dict

    # advanced (need not learn)
    def _build_frequency_dict_2b_2(self, my_words: List[str], excluded_words: List[str]) -> Dict[str, int]:
        return {word: my_words.count(word) for word in set(my_words) if word not in set(excluded_words)}

    def _get_max_value_key_1a(self, my_dict: Dict[str, int]) -> str:
        max_value: int = -1

        # find maximum value
        for value in my_dict.values():
            max_value: int = max(max_value, value)

        # find key corresponding to max_value
        for key, value in my_dict.items():
            if value == max_value:
                return key

        # unreachable statement
        return ""

    def _get_max_value_key_1b(self, my_dict: Dict[str, int]) -> str:
        max_value: int = -1
        key_for_max_value: str = ""

        # find maximum value
        for key, value in my_dict.items():
            if value > max_value:
                max_value: int = value
                key_for_max_value: str = key

        return key_for_max_value

    def _get_max_value_key_2a(self, my_dict: Dict[str, int]) -> str:
        my_swapped_tuples: List[Tuple[int, str]] = [(value, key) for key, value in my_dict.items()]

        # if len(my_swapped_tuples) == 0:
        #     return ""
        if not my_swapped_tuples:
            return ""

        return max(my_swapped_tuples)[1]

    def _get_max_value_key_2b(self, my_dict: Dict[str, int]) -> str:
        my_swapped_tuples: List[Tuple[int, str]] = [tuple(reversed(my_tuple)) for my_tuple in my_dict.items()]
        if len(my_swapped_tuples) == 0:
            return ""
        return max(my_swapped_tuples)[1]

    def _get_max_value_key_2c(self, my_dict: Dict[str, int]) -> str:
        my_swapped_tuples: List[Tuple[int, str]] = list(map(lambda my_tuple: tuple(reversed(my_tuple)), my_dict.items()))
        if not my_swapped_tuples:
            return ""
        return max(my_swapped_tuples)[1]

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words: List[str] = re.split(pattern=Solution.PUNCTUATION_CHARS, string=paragraph.lower())
        non_empty_words: List[str] = list(filter(lambda word: word != "", words))
        # non_empty_words: List[str] = [word for word in words if word != ""]

        # equivalent to this for loop:
        # result = []
        # for word in words:
        #     if word:  # (Empty strings are falsy in Python)
        #         result.append(word)

        freq_dict: Dict[str, int] = self._build_frequency_dict_1a(my_words=non_empty_words, excluded_words=banned)
        print(f"freq_dict = {freq_dict}")

        return self._get_max_value_key_2b(my_dict=freq_dict)


class SolutionTest:
    def test__get_max_value_key(self) -> None:
        soln: Solution = Solution()
        my_dict: Dict[str, int]
        key_out_expected: str
        key_out_computed: str

        my_dict = {}
        key_out_expected = ""
        key_out_computed = soln._get_max_value_key_1a(my_dict=my_dict)
        assert key_out_expected == key_out_computed

        my_dict = {
            "cat": 4,
            "dog": 2,
            "cow": 9
        }
        key_out_expected = "cow"
        key_out_computed = soln._get_max_value_key_1b(my_dict=my_dict)
        assert key_out_expected == key_out_computed

        my_dict = {
            "cat": 2,
            "cow": 9,
            "dog": 4
        }
        key_out_expected = "cow"
        key_out_computed = soln._get_max_value_key_2a(my_dict=my_dict)
        assert key_out_expected == key_out_computed

        my_dict = {
            "cat": 9,
            "cow": 2,
            "dog": 4
        }
        key_out_expected = "cat"
        key_out_computed = soln._get_max_value_key_2b(my_dict=my_dict)
        assert key_out_expected == key_out_computed

        my_dict = {
            "cat": 9,
            "cow": 2,
            "dog": 14
        }
        key_out_expected = "dog"
        key_out_computed = soln._get_max_value_key_2c(my_dict=my_dict)
        assert key_out_expected == key_out_computed

    def test_mostCommonWord(self) -> None:
        soln: Solution = Solution()
        paragraph_in: str
        banned_words_in: List[str]
        word_out_expected: str
        word_out_computed: str

        # paragraph_in = "Bob hit a ball, the hit BALL flew far after it was hit."
        # banned_words_in = ["hit"]
        # word_out_expected = "ball"
        # word_out_computed = soln.mostCommonWord(paragraph=paragraph_in, banned=banned_words_in)
        # # print(f"expected={word_out_expected}, computed={word_out_computed}")
        # assert word_out_expected == word_out_computed
        #
        # paragraph_in = "a."
        # banned_words_in = []
        # word_out_expected = "a"
        # word_out_computed = soln.mostCommonWord(paragraph=paragraph_in, banned=banned_words_in)
        # assert word_out_expected == word_out_computed

        paragraph_in = "Bob. hIt, baLl"
        banned_words_in = ["bob", "hit"]
        word_out_expected = "ball"
        word_out_computed = soln.mostCommonWord(paragraph=paragraph_in, banned=banned_words_in)
        assert word_out_expected == word_out_computed


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()

    soln_test.test__get_max_value_key()
    soln_test.test_mostCommonWord()
