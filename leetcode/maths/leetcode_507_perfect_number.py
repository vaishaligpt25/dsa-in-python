#leetcode_507:-https://leetcode.com/problems/perfect-number

from typing import List

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if num <= 1:
            return False

        divisor_sum = 1
        # only need to check up to square of num for efficiency
        for i in range(2, int(num** .5) + 1):
            if num % i == 0:
                # (add both divisors(the smaller and larger ones)
               divisor_sum += i
                # Add the pair divisor if it's different from i
               if i != num // i:
                  divisor_sum += num // i
        # Number is perfect if sum of its proper divisors equals itself
        return divisor_sum == num


class SolutionTest:
    def test_checkPerfectNumber(self) -> None:
        soln: Solution = Solution()
        assert soln.checkPerfectNumber(num=28) == True

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_checkPerfectNumber()



