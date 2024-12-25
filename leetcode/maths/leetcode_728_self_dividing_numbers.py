# leetcode -728: https://leetcode.com/problems/self-dividing-numbers

from typing import Set, List

class Solution:
    def _getDigits_string(self, num: int) -> Set[int]:
        return {int(digit) for digit in str(num)}

    def _getDigits_numeric(self, num: int) -> Set[int]:
        digits: Set[int] = set()
        while num > 0:
            digit: int = num % 10
            num: int = num / 10
            digits.add(digit)
        return digits

    def _isSelfDividing(self, num: int) -> bool:
        digits: Set[int] = self._getDigits_string(num)
        if 0 in digits:
            return False

        for digit in digits:
            if (num % digit) != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        myList: List[int] = []
        for num in range(left, right + 1):
            if self._isSelfDividing(num):
                myList.append(num)
        return myList

def output_selfDividingNumbers(left: int, right: int) -> None:
   soln: Solution = Solution()
   numbers: List[int] = soln.selfDividingNumbers(left=left, right=right)
   print(f"self dividing numbers in range [{left}, {right}] are: " + str(numbers))

if __name__ == '__main__':
    output_selfDividingNumbers(1, 100)
    output_selfDividingNumbers(1, 22)
    output_selfDividingNumbers(47, 85)
