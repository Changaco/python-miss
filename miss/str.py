
def pstrip(s, prefix):
    """Prefix strip

    >>> pstrip('foo_oof', 'foo_')
    'oof'
    >>> pstrip('baroof', 'foo_')
    'baroof'
    """
    i = len(prefix)
    if s[:i] == prefix:
        return s[i:]
    return s

def sstrip(s, suffix):
    """Suffix strip

    >>> sstrip('foo.oof', '.oof')
    'foo'
    >>> sstrip('baroof', '.oof')
    'baroof'
    """
    i = - len(suffix)
    if s[i:] == suffix:
        return s[:i]
    return s
