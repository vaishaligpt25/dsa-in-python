class Solution:
    def maxBottlesDrunk(self, numFullBottles: int, numExchange: int) -> int:
        numBottlesDrunk: int = 0
        numEmptyBottles: int = 0

        while (numFullBottles > 0) or (numEmptyBottles >= numExchange):
            if numFullBottles > 0:
                numBottlesDrunk: int = numBottlesDrunk + numFullBottles
                numEmptyBottles: int = numEmptyBottles + numFullBottles
                numFullBottles: int = 0

            while numEmptyBottles >= numExchange:
                numEmptyBottles: int = numEmptyBottles - numExchange
                numFullBottles: int = numFullBottles + 1
                numExchange: int = numExchange + 1

        return numBottlesDrunk


def test_num_water_bottles():
    soln: Solution = Solution()

    assert soln.maxBottlesDrunk(numFullBottles=13, numExchange=6) == 15
    assert soln.maxBottlesDrunk(numFullBottles=10, numExchange=3) == 13
    assert soln.maxBottlesDrunk(numFullBottles=10, numExchange=2) == 13

if __name__ == '__main__':
    test_num_water_bottles()
