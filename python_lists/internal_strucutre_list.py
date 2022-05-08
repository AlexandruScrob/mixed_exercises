import sys


def list_internal_structure():
    # Garbage collection info (before object)
    _gc_next = ...  # 8 bytes
    _gc_prev = ...  # 8 bytes

    # PyObject info
    ob_refcnt = ...  # 8 bytes
    ob_type = ...  # 8 bytes

    # PyVarObject info
    ob_size = ...  # len()  # 8 bytes

    # PyListObject info
    ob_item = ...  # pointer to contiguous memory # 8 bytes
    allocated = ...  # how many elems COULD fit in ob_item memory # 8 bytes

    def getsizeof_list():
        n = 56
        n += 8 * allocated


def capacity(l: list):
    return (sys.getsizeof(l) - 56) // 8


def capacity_of_some_lists():
    x = []
    print(capacity(x))  # 0

    for i in range(100):
        x.append(i)
        # NOTE
        print(f"{len(x)=}, {capacity(x)=}")
        # when we hit a capacity limit, python allocates more memory


def compute_overallocation_ratios():
    x = [0]
    last_capacity = 1
    for _ in range(100000):
        x.append(0)
        new_capacity = capacity(x)
        if new_capacity != last_capacity:
            print(f"ratio: {new_capacity/last_capacity:.3f}")
            last_capacity = new_capacity

    print(f"approaching {9/8=}")


def sizeof_some_lists():
    print(sys.getsizeof([]))  # 56 bytes (7 fields * 8 bytes)


def main():
    sizeof_some_lists()
    print()
    # capacity_of_some_lists()
    # print()
    compute_overallocation_ratios()


if __name__ == "__main__":
    main()
