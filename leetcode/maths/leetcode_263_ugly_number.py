#leetcode_263:-https://leetcode.com/problems/ugly-number

class Solution:
    def isUgly(self, n: int) -> bool:
        return self.verify_prime_factors(n=n)

    def verify_prime_factors(self, n: int) -> bool:
        if n <= 0:
            return False

        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime
                #n = n // prime
        return n == 1

class SolutionTest:
    def test_verify_prime_factors(self) -> None:
        soln: Solution = Solution()
        n_in: int
        result_out_expected: bool
        result_out_computed: bool

        n_in = 6
        result_out_expected = True
        result_out_computed = soln. isUgly(n=n_in)
        assert result_out_expected == result_out_computed

        n_in = 14
        result_out_expected = False
        result_out_computed = soln.isUgly(n=n_in)
        assert result_out_expected == result_out_computed


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_verify_prime_factors()







