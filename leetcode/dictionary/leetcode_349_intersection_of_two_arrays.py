# leetcode_349:-https://leetcode.com/problems/intersection-of-two-arrays

from typing import List, Dict, Set


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        return list(nums1Set.intersection(nums2Set))

    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set: Set[int] = set(nums1)
        result: List[int] = []

        for n in nums2:
            if n in nums1_set:
              result.append(n)
              nums1_set.remove(n)
        return result


class SolutonTest:
    def check_intersection(self) -> None:
        soln: Solution = Solution()
        # assert soln.intersection(nums1 = [1,2,2,1], nums2 = [2,2]) == [2]
        # assert set(soln.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])) == {4, 9}
        # assert soln.intersection(nums1 = [4,9,5], nums2 = [1, 2, 3]) == []

        assert soln.intersection1(nums1=[1, 2, 2, 1], nums2=[2, 2]) == [2]
        assert set(soln.intersection1(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])) == {4, 9}
        assert soln.intersection1(nums1=[4, 9, 5], nums2=[1, 2, 3]) == []


if __name__ == '__main__':
    soln_test : SolutonTest = SolutonTest()
    soln_test.check_intersection()

