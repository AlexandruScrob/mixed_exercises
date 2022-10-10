from typing import Iterator


def get_values():
    yield "hello"
    yield "world"
    yield 123


def example_get_values():
    # gen = get_values()
    # print(gen)
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    for x in get_values():
        print(x)


example_get_values()


class Range:
    def __init__(self, stop: int) -> None:
        self.start = 0
        self.stop = stop

    def __iter__(self) -> Iterator[int]:
        curr = self.start
        while curr < self.stop:
            yield curr
            curr += 1


def range_example():
    for n in Range(5):
        print(n)


range_example()
