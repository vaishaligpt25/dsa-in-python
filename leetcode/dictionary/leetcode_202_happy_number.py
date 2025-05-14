# leetcode_202:https://leetcode.com/problems/happy-number


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum_of_squares(num: int) -> int:
            total: int = 0
            while num > 0:
                digit: int = num % 10
                total += digit * digit
                num //= 10
            return total

        seen: set = set()
        while n != 1:
            n = get_sum_of_squares(n)
            if n in seen:
                return False
            seen.add(n)
        return True
