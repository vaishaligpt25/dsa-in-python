class Solution:
    def _sum_of_digit(self, n: int) -> int:
        sum_of_digit: int = 0
        while n > 0:
            last_digit: int = n % 10
            n: int = int(n / 10)
            sum_of_digit: int = sum_of_digit + last_digit
        return sum_of_digit

    def addDigits(self, num: int) -> int:
        while num >= 10:
            num: int = self._sum_of_digit(num)

        return num
