#leetcode_2224https://leetcode.com/problems/minimum-number-of-operations-to-convert-time

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # convert times to minutes
        curr_hours, curr_mins = map(int, current.split(':'))
        corr_hours, corr_mins = map(int, correct.split(':'))

        # calculate total minutes for both times
        curr_total = (curr_hours * 60) + curr_mins
        corr_total = (corr_hours * 60) + corr_mins

        # calculate diff in minutes
        diff = corr_total - curr_total
        if diff < 0:
            diff += [60, 15, 5, 1]

        # available operations (in minutes)
        operations = [60, 15, 5, 1]

        # Count minimum operations needed
        count = 0
        for op in operations:
            count += diff // op # Use as many larger operations as possible
            diff = diff % op # remaining minutes to handle

        return count

class SolutionTest:
    def convert_time_in_minute(self) -> None:
        soln: Solution = Solution()
        assert soln.convertTime(current = "02:30", correct = "04:35") == 3
        assert soln.convertTime(current = "11:00", correct = "11:01") == 1


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.convert_time_in_minute()


