import collections

# similar to async -> async coroutines are defined in terms of generators
def worker(f):
    tasks = collections.deque()
    value = None
    while True:
        batch = yield value
        value = None

        if batch is not None:
            tasks.extend(batch)
        elif tasks:
            args = tasks.popleft()
            value = f(*args)


def example_worker():
    w = worker(str)
    w.send(None)
    w.send([(1,), (2,), (3,)])
    print(next(w))
    print(next(w))
    print(next(w))
    w.send([(4,), (5,)])
    print(next(w))
    print(next(w))
    # w.throw(ValueError)
    w.close()


example_worker()
