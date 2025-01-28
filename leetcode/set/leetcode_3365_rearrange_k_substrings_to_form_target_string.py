from typing import List, Dict


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        slice_list_s: List[str] = self.slicing_of_string(my_string=s, number_of_slices=k)
        slice_list_t: List[str] = self.slicing_of_string(my_string=t, number_of_slices=k)
        s_dict: Dict[str, int] = self.create_freq_map_of_slices(slice_list_s=slice_list_s)
        t_dict: Dict[str, int] = self.create_freq_map_of_slices(slice_list_s=slice_list_t)
        return s_dict == t_dict

    def slicing_of_string(self, my_string: str, number_of_slices: int) -> List[str]:
        slice_size: int = int(len(my_string) / number_of_slices)
        slices: List[str] = []
        for i in range(0, len(my_string), slice_size):
            substring = my_string[i: (i + slice_size)]
            slices.append(substring)
        return slices

    def slicing_of_string_2(self, my_string: str, slice_size: int) -> List[str]:
        return [my_string[i: (i + slice_size)] for i in range(0, len(my_string), slice_size)]

    def create_freq_map_of_slices(self, slice_list_s: List[str]) -> Dict[str, int]:
        s_dict: Dict[str, int] = {}
        for i in range(0, len(slice_list_s)):
            crr_slice: str = slice_list_s[i]
            crr_freq: int = s_dict.get(crr_slice, 0)
            s_dict[crr_slice]: int = crr_freq + 1
        return s_dict

    def create_freq_map_of_slices_2(self, slices: List[str]) -> Dict[str, int]:
        frequencies: Dict[str, int] = {}
        for crr_slice in slices:
            crr_freq: int = frequencies.get(crr_slice, 0)
            frequencies[crr_slice]: int = crr_freq + 1
        return frequencies


class SolutionTest:
    def test_substrings(self) -> None:
        soln: Solution = Solution()
        assert soln.isPossibleToRearrange(s="abcd", t="cdab", k=2) == True
        assert soln.isPossibleToRearrange(s="aabbcc", t="bbaacc", k=2) == False
        assert soln.isPossibleToRearrange(s="aabbcc", t="bbaacc", k=3) == True


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_substrings()
