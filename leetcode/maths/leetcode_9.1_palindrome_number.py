class Solution:
    def isPalindrome(self, x: int) -> bool:
        return self.reversed(x=x)

    def reversed(self, x: int) -> bool:
        if x < 0:
            return False

        original: int = x
        reversed_num: int = 0

        while x > 0:
            digit: int = x % 10
            x: int = int(x / 10)
            reversed_num: int = (reversed_num * 10) + digit

        return original == reversed_num


class SolutionTest:
    def test_reversed(self) -> None:
        soln: Solution = Solution()
        x_in: int
        result_out_expected: bool
        result_out_computed: bool

        x_in = 121
        result_out_expected = True
        result_out_computed = soln.reversed(x=x_in)
        assert result_out_expected == result_out_computed


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_reversed()
