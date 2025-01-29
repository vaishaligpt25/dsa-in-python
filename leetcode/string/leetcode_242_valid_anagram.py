# leetcode_242:-https://leetcode.com/problems/valid-anagram/description/?envType=problem-list-v2&envId=string

from typing import  Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early return if lengths differ
        if len(s) != len(t):
            return False

        # freq_dict_s = self._create_frequency_map(my_str=s)
        # freq_dict_t =self._create_frequency_map(my_str=t)
        # return freq_dict_s == freq_dict_t

        if len(s) != len(t):
            return False

        # create frequency map for both strings
        freq_s = {}
        freq_t = {}

        #build freq maps:
        for i in range(len(s)):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1

        #compare the freq maps
        return freq_s == freq_t

    # def _create_frequency_map(self, my_str: str) -> Dict[str, int]:
    #     freq_dict: Dict[str, int] = {}
    #
    #     for char in my_str:
    #         freq_dict[char] = freq_dict.get(char, 0) + 1
    #     return freq_dict

class SolutionTest:
    def test_isAnagram(self) -> None:
        soln: Solution = Solution()
        assert soln.isAnagram(s = "anagram", t = "nagaram") == True
        assert soln.isAnagram(s="vaishali", t="shvaiali") == True
        assert soln.isAnagram(s = "rat", t = "car") == False
        assert soln.isAnagram(s = "", t = "") == True
        assert soln.isAnagram(s = "rat", t = "ra") == False
        assert soln.isAnagram(s = "aabbb", t = "aaabb") == False


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_isAnagram()

