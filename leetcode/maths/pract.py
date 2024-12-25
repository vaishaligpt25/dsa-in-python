def perfect_square(n:int) ->int:
    if n < 1:
        return False
    i: int= 1

    while ( i* i) <= n:
        if (i * i) == n:
            return True
        i += 1
    return False

def output_perfect_square(n:int) ->None:
    if perfect_square(n):
        print(f"{n} is perfect square")
    else:
        print(f"{n} is not perfect square")

if __name__ == '__main__':
    output_perfect_square(100)
    output_perfect_square(256)
    output_perfect_square(254)


