# leetcode_944:- https://leetcode.com/problems/delete-columns-to-make-sorted
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete_count = 0
        # get length of each string( all have same length)
        str_len = len(strs[0])

        #check each column
        for column in range(str_len):
            #check if column is sorted
            for row in range(1, len(strs)):
                if strs[row][column] < strs[row - 1][column]:
                    delete_count += 1
                    break

        return delete_count

class SolutionTest:
    def test_minDeletionSize(self) -> None:
        solution = Solution()
        assert solution.minDeletionSize(["cba","daf","ghi"]) == 1
        assert solution.minDeletionSize(["a", "b"]) == 0


if __name__ == '__main__':
    solution_test = SolutionTest()
    solution_test.test_minDeletionSize()



