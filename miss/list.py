
concat = lambda l: reduce(list.__add__, l, [])

def grow(l, size, filler=None):
    """Grow the list $l to $size filling with $filler.
    >>> grow(list(range(5)), 4)
    [0, 1, 2, 3, 4]
    >>> grow(list(range(5)), 5)
    [0, 1, 2, 3, 4]
    >>> grow(list(range(5)), 6)
    [0, 1, 2, 3, 4, None]
    >>> grow(list(range(5)), 7, lambda i: i)
    [0, 1, 2, 3, 4, 5, 6]
    """
    ll = len(l)
    if ll < size:
        if callable(filler):
            return l + [filler(i) for i in range(ll, size)]
        else:
            return l + [filler]*(size-ll)
    else:
        return l

singleton = lambda a: [a]
