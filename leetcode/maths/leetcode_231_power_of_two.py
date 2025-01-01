#leetcode-231: https://leetcode.com/problems/power-of-two

def PowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False

    while n > 1:
        if n % 2 != 0:
            return False
        n = n / 2
    return True


def output_PowerOfTwo(n: int) -> None:
    if PowerOfTwo(n=n):
        print(f"number {n} is power of 2")
    else:
        print(f"number {n} is NOT power of 2")


if __name__ == '__main__':
    output_PowerOfTwo(16)
    output_PowerOfTwo(25)
    output_PowerOfTwo(300)
    output_PowerOfTwo(400)
    output_PowerOfTwo(1)
    output_PowerOfTwo(2)
    output_PowerOfTwo(4)
    output_PowerOfTwo(8)
    output_PowerOfTwo(1024)
