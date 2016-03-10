
from .six.moves import reduce


def getattrs(o, *attrs, **kwargs):
    """
    >>> getattrs((), '__iter__', '__name__', 'strip')('_')
    'iter'
    >>> getattrs((), 'foo', 'bar', default=0)
    0
    """
    if 'default' in kwargs:
        default = kwargs['default']
        c = o
        for attr in attrs:
            try:
                c = getattr(c, attr)
            except AttributeError:
                return default
        return c
    else:
        return reduce(getattr, attrs, o)
