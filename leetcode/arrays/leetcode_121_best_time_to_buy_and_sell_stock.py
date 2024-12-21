# LeetCode-121: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        max_price_on_right: int = 0
        max_profit_so_far: int = 0

        for i in range(len(prices) - 1, -1, -1):
            crr_price: int = prices[i]

            crr_max_profit: int = max_price_on_right - crr_price
            max_profit_so_far: int = max(max_profit_so_far, crr_max_profit)

            max_price_on_right: int = max(max_price_on_right, crr_price)

        return max_profit_so_far

class SolutionTest:
    def test_maxProfit(self) -> None:
        soln: Solution = Solution()

        assert soln.maxProfit(prices=[7,1,5,3,6,4]) == 5
        assert soln.maxProfit(prices=[7,6,4,3,1]) == 0
        assert soln.maxProfit(prices=[]) == 0
        assert soln.maxProfit(prices=[4]) == 0
        assert soln.maxProfit(prices=[4, 4, 4]) == 0

if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.test_maxProfit()
