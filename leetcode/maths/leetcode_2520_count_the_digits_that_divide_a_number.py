# leetcode_2520:-https://leetcode.com/problems/count-the-digits-that-divide-a-number

class Solution:
    def countDigits(self, num: int) -> int:
        # store original number since we will modify temp
        total_count: int = 0
        temp: int = num

        # Extract each digit and check if it divides num
        while temp > 0:
            digit: int = temp % 10
            if digit != 0 and num % digit == 0:
                total_count += 1
            temp //= 10
        return total_count


class SolutionTest:
    def countDigits(self) -> None:
        soln: Solution = Solution()
        assert soln.countDigits(num=7) == 1
        assert soln.countDigits(num=121) == 2
        assert soln.countDigits(num=0) == 0
        assert soln.countDigits(num=1000) == 1


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.countDigits()
