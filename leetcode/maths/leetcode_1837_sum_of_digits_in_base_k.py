class Solution:
    def _convert_to_base(self, num_base_10: int, k: int) -> int:
        num_base_k: int = 0
        pow_of_10: int = 1
        while num_base_10 > 0:
            remainder: int = num_base_10 % k
            num_base_10: int = int(num_base_10 / k)

            num_base_k: int = num_base_k + (remainder * pow_of_10)
            pow_of_10: int = pow_of_10 * 10
        return num_base_k

    def _sum_of_digits(self, num: int) -> int:
        sum: int = 0
        while num > 0:
            digit: int = num % 10
            num: int = int(num / 10)
            sum: int = sum + digit
        return sum

    def sumBase(self, n: int, k: int) -> int:
        n_in_base_k: int = self._convert_to_base(num_base_10=n, k=k)
        return self._sum_of_digits(num=n_in_base_k)

def test__convert_to_base() -> None:
    soln: Solution = Solution();

    assert soln._convert_to_base(num_base_10=5186, k=10) == 5186
    assert soln._convert_to_base(num_base_10=5186, k=6) == 40002
    assert soln._convert_to_base(num_base_10=5186, k=4) == 1101002
    assert soln._convert_to_base(num_base_10=5186, k=8) == 12102
    assert soln._convert_to_base(num_base_10=5186, k=9) == 7102
    assert soln._convert_to_base(num_base_10=1, k=2) == 1
    assert soln._convert_to_base(num_base_10=1, k=10) == 1
    assert soln._convert_to_base(num_base_10=34, k=6) == 54
    assert soln._convert_to_base(num_base_10=100, k=2) == 1100100

def test__sum_of_digits() -> None:
    soln: Solution = Solution()

    assert soln._sum_of_digits(num=0) == 0
    assert soln._sum_of_digits(num=6) == 6
    assert soln._sum_of_digits(num=10) == 1
    assert soln._sum_of_digits(num=9999) == 36
    assert soln._sum_of_digits(num=2147483647) == 46

def test__sumBase() -> None:
    soln: Solution = Solution()

    assert soln.sumBase(n=34, k=6) == 9
    assert soln.sumBase(n=10, k=10) == 1
    assert soln.sumBase(n=100, k=2) == 3

if __name__ == '__main__':
    test__convert_to_base()
    test__sum_of_digits()
    test__sumBase()
