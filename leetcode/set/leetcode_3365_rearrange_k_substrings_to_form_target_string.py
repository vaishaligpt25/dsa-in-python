from typing import List, Dict

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        slice_list_s: List[str] = self.slicing_of_string(s=s, k=k)
        slice_list_t: List[str] = self.slicing_of_string(s=t, k= k)

        s_dict: Dict[str, int] = self.create_dict_of_slice_list_s(slice_list_s= slice_list_s)
        t_dict: Dict[str, int] = self.create_dict_of_slice_list_s(slice_list_s= slice_list_t)

        return s_dict == t_dict


    def slicing_of_string(self, s: str, k: int) -> List[str]:
        slice_list_s: List[str] = []
        for i in range(0, len(s), k):
             substring = s[i: (i + k)]
             slice_list_s.append(substring)
        return slice_list_s

    def create_dict_of_slice_list_s(self, slice_list_s: List[str]) -> Dict[str, int]:
        s_dict: Dict[str, int] = {}
        for i in range(0, len(slice_list_s)):
            crr_slice: str = slice_list_s[i]
            crr_freq: int = s_dict.get(crr_slice, 0)
            s_dict[crr_slice]: int = crr_freq + 1
        return s_dict



class SolutionTest:
    def test_substrings(self) -> None:
        soln: Solution= Solution()
        assert soln.isPossibleToRearrange(s = "abcd", t = "cdab", k= 2) == True
        assert soln.isPossibleToRearrange(s = "aabbcc", t = "bbaacc", k= 2) == True
        assert soln.isPossibleToRearrange(s="aabbcc", t="bbaacc", k=3) == False


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_substrings()

