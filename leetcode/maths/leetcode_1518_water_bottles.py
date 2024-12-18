class Solution:
    def numWaterBottles(self, numFullBottles: int, numExchange: int) -> int:
        numBottlesDrunk: int = 0
        numEmptyBottles: int = 0

        while (numFullBottles > 0) or (numEmptyBottles >= numExchange):
            if numFullBottles > 0:
                numBottlesDrunk: int = numBottlesDrunk + numFullBottles
                numEmptyBottles: int = numEmptyBottles + numFullBottles
                numFullBottles: int = 0

            if numEmptyBottles >= numExchange:
                numFullBottles: int = int(numEmptyBottles / numExchange)
                numEmptyBottles: int = numEmptyBottles % numExchange

        return numBottlesDrunk


def test_num_water_bottles():
    soln: Solution = Solution()

    assert soln.numWaterBottles(numFullBottles=6, numExchange=3) == 8
    assert soln.numWaterBottles(numFullBottles=9, numExchange=3) == 13
    assert soln.numWaterBottles(numFullBottles=15, numExchange=4) == 19
    assert soln.numWaterBottles(numFullBottles=1, numExchange=2) == 1
    assert soln.numWaterBottles(numFullBottles=100, numExchange=100) == 101
    assert soln.numWaterBottles(numFullBottles=100, numExchange=50) == 102
    assert soln.numWaterBottles(numFullBottles=100, numExchange=25) == 104
    assert soln.numWaterBottles(numFullBottles=100, numExchange=10) == 111
    assert soln.numWaterBottles(numFullBottles=100, numExchange=2) == 199

if __name__ == '__main__':
    test_num_water_bottles()
