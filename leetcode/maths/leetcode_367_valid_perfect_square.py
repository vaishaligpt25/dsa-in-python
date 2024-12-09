#leetcode-367: https://leetcode.com/problems/valid-perfect-square


def perfect_square(n: int) -> bool:
    if n < 1:
        return False

    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1


def output_perfect_square(n: int) -> None:
    if perfect_square(n):
        print(n, "is perfect square")
    else:
        print(n, "is not perfect square")


if __name__ == '__main__':
    output_perfect_square(49)
    output_perfect_square(256)
    output_perfect_square(280)
    output_perfect_square(400)
