def f():
    pass


def g():
    pass


def default():
    pass


# jump table-like
_switch_dict = {0: f, 1: g, 2: g, 3: f}


def switch_dict_example(x):
    do_next = _switch_dict.get(x, default=default)
    do_next()
