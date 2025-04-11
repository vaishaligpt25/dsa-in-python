# https://leetcode.com/problems/check-if-the-number-is-fascinating/


class Solution:
    def isFascinating(self, n: int) -> bool:
        concatenated = str(n) + str(2 * n) + str(3 * n)

        if len(concatenated) != 9:
            return False

        counts = {}
        for digit in concatenated:
            if digit == '0' or digit in counts:
                return False
            counts[digit] = 1
        return len(counts) == 9
