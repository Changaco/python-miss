
concat = lambda l: reduce(list.__add__, l, [])

def grow(l, size, filler=None):
    """Grow the list $l to $size filling with $filler.
    >>> grow(range(5), 4)
    [0, 1, 2, 3, 4]
    >>> grow(range(5), 5)
    [0, 1, 2, 3, 4]
    >>> grow(range(5), 6)
    [0, 1, 2, 3, 4, None]
    """
    ll = len(l)
    if ll < size:
        return l + [filler]*(size-ll)
    else:
        return l

singleton = lambda a: [a]
