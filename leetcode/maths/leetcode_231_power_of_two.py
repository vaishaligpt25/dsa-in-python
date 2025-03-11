# https://leetcode.com/problems/power-of-two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 2 != 0:
                return False
            n = n // 2 # Using integer division instead of float division
        return True
