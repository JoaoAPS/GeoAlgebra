from numbers import Number


def is_number(x):
    return isinstance(x, Number) and not isinstance(x, bool)
