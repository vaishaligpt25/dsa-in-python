# LeetCode-509: https://leetcode.com/problems/fibonacci-number

def get_nth_fibnocci (n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1

    fib1: int = 1
    fib2: int = 1
    for i in range(3, n+1) :
        fib3 = fib1 + fib2

        fib1 = fib2
        fib2 = fib3

    return fib2

def output_nth_fibnocci (n: int) -> None :
    fib  : int = get_nth_fibnocci(n)
    print(f"fibonacci number {n} is {fib} ")

if __name__ == '__main__':
    output_nth_fibnocci(1)
    output_nth_fibnocci(2)
    output_nth_fibnocci(3)
    output_nth_fibnocci(50)
    output_nth_fibnocci(23)
    output_nth_fibnocci(5)
