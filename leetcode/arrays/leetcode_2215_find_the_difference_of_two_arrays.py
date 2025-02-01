#leetcode_2215:-https://leetcode.com/problems/find-the-difference-of-two-arrays
from threading import main_thread
from typing import List, Set, Dict

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_map: Dict[int, int] = {}
        nums2_map: Dict[int, int] = {}

        # Populate first map
        for num in nums1:
            nums1_map[num] = nums1_map.get(num, 0) + 1

        # Populate second map
        for num in nums2:
            nums2_map[num] = nums2_map.get(num, 0) + 1

        # Find elements unique to nums1
        ans1: List[int] = []
        for num in nums1_map:
            if num not in nums2_map:
               ans1.append(num)

        #find elements unique to nums2
        ans2: List[int] = []
        for num in nums2_map:
            if num not in nums1_map:
                ans2.append(num)
        return [ans1, ans2]


    def findDifference1(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1: Set[int] = set(nums1)
        set2: Set[int] = set(nums2)

        return [list(set1- set2), list(set2- set1)]


class SolutionTest:
    def check_difference_of_two_arrays(self) -> None:
        soln: Solution = Solution()
        assert soln.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]) == [[1,3],[4,6]]
        assert soln.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]) == [[3],[]]

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_difference_of_two_arrays()

