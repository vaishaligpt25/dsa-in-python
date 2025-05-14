# leetcode_14_https://leetcode.com/problems/longest-common-prefix
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # handle edge cases:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        shortest_string_length:int = min(len(s) for s in strs)
        for i in range(shortest_string_length):
            char:str = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    return strs[0][:i]
        return strs[0][:shortest_string_length]

