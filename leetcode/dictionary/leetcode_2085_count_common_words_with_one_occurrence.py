#leetcode_2085https://leetcode.com/problems/count-common-words-with-one-occurrence

from typing import List, Dict, Set


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # create frequency map for both dictionaries
        freq1: Dict[str, int] = {}
        freq2: Dict[str, int] = {}

        # Count frequencies in words1
        for word in words1:
            freq1[word] = freq1.get(word, 0) + 1

        for word in words2:
            freq2[word] = freq2.get(word, 0) + 1

        # count word that exactly occure once in both list
        count = 0
        for word in freq1:
            if freq1[word] == 1 and word in freq2 and freq2[word] == 1:
                count += 1

        return count








