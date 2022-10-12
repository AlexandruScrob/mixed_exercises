def from_generator():
    # bonus funnctionality
    # for sq in (x * x for x in range(5)):
    #   yield sq
    yield from (x * x for x in range(5))
    # yield from facilitates the bidirectionl nature of generators
    # (get values and sends values)
    # takes messages from worker and yield them up to the caller
