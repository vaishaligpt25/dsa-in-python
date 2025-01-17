#leetcode_412:-https://leetcode.com/problems/fizz-buzz

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return self.create_list(n=n)


    def create_list(self, n: int) -> List[str]:
        result = []
        for i in range (1 , n + 1):
            modulus_3 = i % 3
            modulus_5 = i % 5
            if modulus_3 == 0 and modulus_5 == 0:
                result.append("FizzBuzz")
            elif modulus_3 == 0:
                result.append("Fizz")
            elif modulus_5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

    def create_list_2(self, n: int) -> List[str]:
        result = []
        for i in range (1 , n + 1):
            is_divisible_by_3: bool = (i % 3) == 0
            is_divisible_by_5: bool = (i % 5) == 0
            if is_divisible_by_3 and is_divisible_by_5:
                result.append("FizzBuzz")
            elif is_divisible_by_3:
                result.append("Fizz")
            elif is_divisible_by_5:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

class SolutionTest:
    def create_list(self) -> None:
        soln: Solution = Solution()
        n_in: int
        result_out_expected: List[str]
        result_out_computed: List[str]

        n_in = 5
        result_out_expected = ["1","2","Fizz","4","Buzz"]
        result_out_computed = soln.create_list(n=n_in)
        # print(f"expected={result_out_expected}, computed={result_out_computed}")
        assert result_out_expected ==  result_out_computed

        n_in =3
        result_out_expected = ["1","2","Fizz"]
        result_out_computed = soln.create_list(n=n_in)
        assert result_out_expected == result_out_computed

        n_in = 1
        result_out_expected = ["1"]
        result_out_computed = soln.create_list(n=n_in)
        assert result_out_expected == result_out_computed

        n_in = 0
        result_out_expected = []
        result_out_computed = soln.create_list(n=n_in)
        assert result_out_expected == result_out_computed

        n_in = 15
        result_out_expected = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
        result_out_computed = soln.create_list(n=n_in)
        assert result_out_expected == result_out_computed




if __name__ == '__main__':
        soln_test: SolutionTest = SolutionTest()

        soln_test.create_list()



