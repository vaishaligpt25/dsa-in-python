# LeetCode-1276: https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

"""
By creating and solving simultaneous linear equations relating
1. t: no of tomato slices
2. c: no of cheese slices
3. j: no of jumbo burgers
4. s: no of small burgers

we get solutions
(a) j = (t - 2c) / 2
(b) s = (4c - t) / 2

so we can proceed as follows
1. calculate j & s using above equations (rounded down to nearest integers)
  - also use basic heuristics for early return such as j & s can't be negative
2. verify that above equations hold true (since we rounded down the results obtained from them)
  - if verification succeeds, return [j, s]
  - otherwise return []
"""

from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if max(tomatoSlices, cheeseSlices) == 0:
            return [0, 0]

        num_jumbo_burgers: int = int((tomatoSlices - (2 * cheeseSlices)) / 2)
        if num_jumbo_burgers < 0:
            return []

        num_small_burgers: int = int(((4 * cheeseSlices) - tomatoSlices) / 2)
        if num_small_burgers < 0:
            return []

        # verify results
        expected_num_tomato_slices: int = (4 * num_jumbo_burgers) + (2 * num_small_burgers)
        expected_num_cheese_slices: int = num_jumbo_burgers + num_small_burgers

        if (tomatoSlices != expected_num_tomato_slices) or (cheeseSlices != expected_num_cheese_slices):
            return []

        return [num_jumbo_burgers, num_small_burgers]
