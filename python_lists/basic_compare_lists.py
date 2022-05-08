import sys

from internal_strucutre_list import capacity


def basic_compare_lists():
    print(sys.getsizeof([0, 0, 0]))  # 120 bytes
    print(sys.getsizeof([0] * 3))  # 80
    print(sys.getsizeof([0] * 8))  # 120
    print(sys.getsizeof([0 for _ in range(3)]))  # 88
    print([0, 0, 0] == [0] * 3 == [0 for _ in range(3)])  # True

    print()
    x = [0, 0, 0]
    n = len(x)
    y = [0] * n
    z = [0 for _ in range(n)]
    x[:] = y[:] = z[:] = [1, 2, 3]
    print(sys.getsizeof(x))  # 120 bytes
    print(sys.getsizeof(y))  # 80
    print(sys.getsizeof(z))  # 88


def basic_compare_lists_with_var():
    e = 0
    x = [e, e, e]
    n = len(x)
    y = [e] * n
    z = [e for _ in range(n)]
    print(sys.getsizeof(x))  # 80 bytes
    print(sys.getsizeof(y))  # 80
    print(sys.getsizeof(z))  # 88


def basic_compare_lists_more_elements():
    x = [0, 0, 0]
    n = len(x)
    y = [0] * n
    z = [0 for _ in range(n)]
    x[:] = y[:] = z[:] = range(1000)
    # they eventually reach same size
    print(sys.getsizeof(x))  # 8056
    print(sys.getsizeof(y))  # 8056
    print(sys.getsizeof(z))  # 8056

    # shrinked they get to same size
    x[:] = y[:] = z[:] = [0, 0, 0]
    print(sys.getsizeof(x))  # 120
    print(sys.getsizeof(y))  # 120
    print(sys.getsizeof(z))  # 120


def basic_compare_lists_capacity():
    x = [0, 0, 0]
    n = len(x)
    y = [0] * n
    z = [0 for _ in range(n)]

    print(capacity(x))  # 8
    print(capacity(y))  # 3
    print(capacity(z))  # 4


def main():
    basic_compare_lists()
    print()
    basic_compare_lists_with_var()
    print()
    basic_compare_lists_more_elements()
    print()
    basic_compare_lists_capacity()


if __name__ == "__main__":
    main()
