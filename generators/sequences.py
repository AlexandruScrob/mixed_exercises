def collatz(n):
    while True:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        yield n

        if n == 1:
            break


def example_collatz():
    n = 27
    seq = list(collatz(n))
    print(seq)


def example_collatz_len():
    n = 27
    print(sum(1 for _ in collatz(n)))


example_collatz()
example_collatz_len()
