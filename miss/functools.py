
def compose(f, g, unpack=False):
    """
    >>> compose(int, str)(0)
    0
    >>> compose(lambda *a: a, lambda *a: a, True)(0, 1)
    (0, 1)
    """
    if unpack:
        return lambda *args, **kwargs: f(*g(*args, **kwargs))
    else:
        return lambda *args, **kwargs: f(g(*args, **kwargs))
