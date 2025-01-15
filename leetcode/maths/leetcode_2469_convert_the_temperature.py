from typing import List

class Solution:

    def convertTemperature(self,celsius: float) -> List[float]:
        return self.convert_temperature(celsius=celsius)

    def convert_temperature(self, celsius: float) -> List[float]:
        kelvin: float = celsius + 273.15
        farenhite: float= celsius* 1.80+ 32.00
        return [kelvin, farenhite]

class SolutionTest:
    def test__convertTemperature(self) -> None:
        soln: Solution = Solution()
        celsius: float
        result_out_expected: List[float]
        result_out_computed: List[float]

        celsius = 36.50
        result_out_expected= [309.65000,97.70000]
        result_out_computed= soln.convert_temperature(celsius= celsius)
        assert result_out_expected == result_out_computed

        celsius = 122.11
        result_out_expected = [395.26000,251.79800]
        result_out_computed = soln.convert_temperature(celsius=celsius)
        assert result_out_expected == result_out_computed

        celsius = 0
        result_out_expected = [273.15, 32.00]
        result_out_computed = soln.convert_temperature(celsius=celsius)
        assert result_out_expected == result_out_computed


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()







