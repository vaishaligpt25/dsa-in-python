from itertools import count
from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count: dict[int, int] = {}
        result: int = 0

        for num in nums:
            if num in count:
                result += count[num]
            count[num] = count.get(num, 0) + 1
        return result


def numIdenticalPairs1(self, nums: List[int]) -> int:
    # Count frequencies of each number
    count = Counter(nums)
    # Calculate pairs using combination formula
    return sum(n * (n - 1) // 2 for n in count.values())
