# leetcode_2248_https://leetcode.com/problems/intersection-of-multiple-arrays

from typing import List, Dict, Set


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        #create dictionary to store frequency of each arrays
        freq: Dict[int, int] = {}
        result: List[int] = []

        n = len(nums) #no. of arrays

        #count frequency of each number across all arrays
        for arr in nums:
            #convert to set to handle duplicates within same array
            for num in set(arr):
                freq[num] = freq.get(num, 0) + 1

        # if a number appears in all arrays, its frequency will equal n
        for num in freq:
            if freq[num] == n:
                result.append(num)

        # return sorted result as per problem requirement
        return sorted(result)

class SolutionTest:
    def check_intersection(self) -> None:
        soln: Solution = Solution()
        assert soln.intersection(nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]) == [3, 4]
        assert soln.intersection(nums = [[1,2,3],[4,5,6]]) == []


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_intersection()






