# https://leetcode.com/problems/top-k-frequent-words

from typing import List, Dict


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = {}

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        sorted_words = sorted(word_freq.keys(), key= lambda x: (-word_freq[x], x))
        return sorted_words[:k]



