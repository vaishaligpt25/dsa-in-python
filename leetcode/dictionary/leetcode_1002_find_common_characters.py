#leetcode_1002:-https://leetcode.com/problems/find-common-characters/description

from typing import List, Dict, Set

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        # initialize with frequencies of first word:
        char_count: Dict[str, int] = {}
        for char in words[0]:
            char_count[char] = char_count.get(char, 0) + 1

        # compare with each subsequent word
        for word in words[1:]:
            # count frequencies in current word
            curr_count = {}
            for char in word:
                curr_count[char] = curr_count.get(char, 0) + 1

            # update char_count to keep minimum frequencies
            for char in list(char_count.keys()):
                if char in curr_count:
                    char_count[char] = min(char_count[char], curr_count[char])
                else:
                    del char_count[char]

        # Convert  frequencies to list of characters
        result = []
        for char, count in char_count.items():
            result.extend([char] * count)

        return result