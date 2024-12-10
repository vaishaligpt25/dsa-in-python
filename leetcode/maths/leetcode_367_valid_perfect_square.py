#leetcode-367: https://leetcode.com/problems/valid-perfect-square


def perfect_square(n: int) -> bool:
    if n < 1:
        return False

    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1

    return False


def output_perfect_square(n: int) -> None:
    if perfect_square(n):
        print(n, "is perfect square")
    else:
        print(n, "is not perfect square")


if __name__ == '__main__':
    output_perfect_square(1)
    output_perfect_square(2)
    output_perfect_square(3)
    output_perfect_square(4)
    output_perfect_square(8)
    output_perfect_square(9)
    output_perfect_square(14)
    output_perfect_square(16)
    output_perfect_square(49)
    output_perfect_square(256)
    output_perfect_square(280)
    output_perfect_square(400)
    output_perfect_square(1296)
