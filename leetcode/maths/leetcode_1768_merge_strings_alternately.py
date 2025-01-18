#leetcode_1768:-https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0

        while i< len(word1) and i< len(word2):
            result.append(word1[i])
            result.append(word2[i])
            i += 1
        # Add remaining characters from word1 if any
        result.append(word1[i:])
        # Add remaining characters from word2 if any
        result.append(word2[i:])

        #join all characters into final string
        return "".join(result)

class SolutionTest:
    def test_mergeAlternately(self):
        soln: Solution = Solution()
        assert soln.mergeAlternately("abc","pqr") == "apbqcr"
        assert soln.mergeAlternately("abcd","pq") == "apbqcd"
        assert soln.mergeAlternately("ab","pqrs") == "apbqrs"

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_mergeAlternately()