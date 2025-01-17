class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        while n > 1:
            if n % 4 != 0:
                return False
            n = n / 4
        return True


class SolutionTest:
    def test_isPowerOfFour(self) -> None:
        soln: Solution = Solution()
        assert soln.isPowerOfFour(n=1) == True
        assert soln.isPowerOfFour(n=6) == False
        assert soln.isPowerOfFour(n=16) == True


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_isPowerOfFour()
