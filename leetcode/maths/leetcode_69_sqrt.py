def mySqrt( n: int) -> int:
    if n <= 1:
        return n

    i: int = 2
    while (i * i) < n:
        i: int = i + 1

    if (i * i) == n:
        return i
    else:
        return i - 1


def output_mySqrt(n: int) -> None:
    i:int = mySqrt(n)
    print(f"{i} is sqrt of {n}")
if __name__ == '__main__':
    output_mySqrt(36)
    output_mySqrt(34)
    output_mySqrt(400)
    output_mySqrt(169)
    output_mySqrt(170)
