def reverse_digits(x: int) -> int:
    x_reversed: int = 0
    while x > 0:
        dig: int = x % 10
        x: int = int(x / 10)
        x_reversed: int = (x_reversed * 10) + dig
    return x_reversed

def output_isPalindrome( x: int) -> None:
    x_reversed : int = reverse_digits(x)
    is_palindrome: bool = x == x_reversed
    print(f"is_palindrome({x}) = {is_palindrome}")

if __name__ == '__main__':
    output_isPalindrome(121)
    output_isPalindrome(123)
    output_isPalindrome(12321)
