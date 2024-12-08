def power_of_three(n: int) -> bool:
    """

    :rtype: object
    """
    if n <= 0:
        return False

    while n > 1:
        if n % 3 != 0:
            return False
        n = n / 3
    return True


def output_power_of_three(n: int) -> None:
    if power_of_three(n=n):
        print(f"number {n} is power of 3")
    else:
        print(f"number {n} is NOT power of 3")


if __name__ == '__main__':
    output_power_of_three(27)
    output_power_of_three(9)
    output_power_of_three(1)
    output_power_of_three(0)
    output_power_of_three(36)
    output_power_of_three(256)
