# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent
from itertools import count


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq1 = {}
        freq2 = {}

        for letter in word1:
            freq1[letter] = freq1.get(letter, 0) + 1

        for letter in word2:
            freq2[letter] = freq2.get(letter, 0) + 1

        for letter in set(word1 + word2):
            count1 = freq1.get(letter, 0)
            count2 = freq2.get(letter, 0)

            if abs(count1 - count2) > 3:
                return False
        return True