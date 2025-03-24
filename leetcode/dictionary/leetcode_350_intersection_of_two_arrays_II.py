#leetcode_350:-https://leetcode.com/problems/intersection-of-two-arrays-ii

from typing import List, Dict, Set


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_map: Dict[int, int] = {}
        result: List[int] = []

        #count frequencies in nums1:
        for num in nums1:
            num_map[num] = num_map.get(num, 0) + 1

        # check nums2 against the map
        for num in nums2:
            if num in num_map and num_map[num] > 0:
                result.append(num)
                num_map[num] -= 1 # decrease count instead of removing
        return result

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
            nums1.sort()
            nums2.sort()
            result: List[int] = []
            i, j = 0, 0

            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    i += 1
                elif nums1[i] > nums2[j]:
                    j += 1
                else:
                    result.append(nums1[i])
                    i += 1
                    j += 1
            return result

class SolutionTest:
    def check_intersection(self) -> None:
        soln: Solution = Solution()
        assert soln.intersect1(nums1 = [1,2,2,1], nums2 = [2,2]) == [2, 2]
        assert soln.intersect1(nums1 = [4,9,5], nums2 = [9,4,9,8,4]) == [4, 9]


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_intersection()
