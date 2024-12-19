# LeetCode-1716: https://leetcode.com/problems/calculate-money-in-leetcode-bank
class Solution:
    DAYS_IN_WEEK: int = 7
    AMOUNT_FIRST_DAY: int = 1
    SUM_FIRST_WEEK: int = 28
    INCREASE_EVERY_DAY: int = 1
    INCREASE_EVERY_WEEK: int = 1

    def totalMoney(self, num_days: int) -> int:
        num_weeks: int = int(num_days / Solution.DAYS_IN_WEEK)
        num_remainder_days: int = num_days % Solution.DAYS_IN_WEEK

        # add up week-wise
        last_week_sum: int = (Solution.SUM_FIRST_WEEK +
                              ((num_weeks - 1) * (Solution.DAYS_IN_WEEK * Solution.INCREASE_EVERY_WEEK)))
        week_wise_sum: int = int((num_weeks * (Solution.SUM_FIRST_WEEK + last_week_sum)) / 2)

        # add up remainder-day-wise
        first_day_amount: int = (num_weeks * Solution.INCREASE_EVERY_WEEK) + Solution.AMOUNT_FIRST_DAY
        last_day_amount: int = first_day_amount + (num_remainder_days - 1) * Solution.INCREASE_EVERY_DAY
        remainder_days_sum: int = int((num_remainder_days * (first_day_amount + last_day_amount)) / 2)

        return week_wise_sum + remainder_days_sum


def test_totalMoney():
    soln: Solution = Solution()

    assert soln.totalMoney(num_days=1) == 1
    assert soln.totalMoney(num_days=2) == 3
    assert soln.totalMoney(num_days=3) == 6
    assert soln.totalMoney(num_days=4) == 10
    assert soln.totalMoney(num_days=5) == 15
    assert soln.totalMoney(num_days=6) == 21
    assert soln.totalMoney(num_days=7) == 28
    assert soln.totalMoney(num_days=8) == 30
    assert soln.totalMoney(num_days=9) == 33
    assert soln.totalMoney(num_days=10) == 37
    assert soln.totalMoney(num_days=20) == 96

if __name__ == '__main__':
    test_totalMoney()
