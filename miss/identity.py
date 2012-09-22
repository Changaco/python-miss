# This file is part of a program licensed under the terms of the GNU Lesser
# General Public License version 3 (or at your option any later version)
# as published by the Free Software Foundation.
#
# If you have not received a copy of the GNU Lesser General Public License
# along with this file, see <http://www.gnu.org/licenses/>.


from .lazy import lazy
from .six import PY3
from .six.moves import reduce


def _derive(cls):
    c = lazy(lambda: type('Identity', (Identity, cls), {}))
    return lambda self: c()(cls)

class Identity(object):
    """The identity element of many basic python operations.

    >>> i = Identity()
    >>> i
    Identity()
    >>> (i + 1) + (2 * i) + (3**i) + (i - 4j) + (i / 2)
    (6-4j)
    >>> i & 1 | 2
    2
    >>> i + []
    []
    >>> print(i.foo()['bar'])
    ?

    Be careful with id comparison ("is" operator),
    we store multiple instances to fake numeric types.
    >>> i is Identity()
    True
    >>> int(i) is int(i)
    True
    >>> i is int(i)
    False

    You can use value comparison instead, it will only return True
    when compared with other instances of Identity subclasses.
    >>> i == int(i)
    True
    >>> i == object()
    False
    """
    def __new__(cls, sup=object):
        if '_inst' in cls.__dict__:
            return cls._inst
        r = cls._inst = sup.__new__(cls)
        return r
    def __getattribute__(self, name):
        if name[0] == '_':
            return object.__getattribute__(self, name)
        return self
    __abs__ = __and__ = __call__ = __delattr__ = __delitem__ = \
    __div__ = __floordiv__ = __getattr__ = __getitem__ = \
    __invert__ = __lshift__ = __mod__ = __neg__ = __pos__= __pow__ = \
    __rand__ = __rshift__ = __setattr__ = __setitem__ = __truediv__ = \
        lambda self, *args, **kwargs: self
    __add__ = __mul__ = __or__ = __radd__ = __rdiv__ = __rfloordiv__ = \
    __rlshift__ = __rrshift__ = __rmod__ = __rmul__ = __ror__ = \
    __rpow__ = __rsub__ = __rtruediv__ = __rxor__ = __xor__ = \
        lambda self, other: other
    __bool__ = __nonzero__ = lambda self: False
    __eq__ = lambda self, other: issubclass(other.__class__, Identity)
    __iter__ = lambda self: iter(())
    __len__ = lambda self: 0
    __repr__ = lambda self: 'Identity()'
    __str__ = lambda self: '?'
    __sub__ = lambda self, other: - other
    __complex__ = _derive(complex)
    __float__ = _derive(float)
    __int__ = __round__ = _derive(int)
    if PY3:
        __bytes__ = lambda self: b'?'
    else:
        __long__ = _derive(long)
        __unicode__ = lambda self: unicode('?')

identity = Identity()


def call(func, obj, default=identity):
    """
    Return func(obj) if obj != identity else return default.
    """
    if obj != identity:
        return func(obj)
    return default


def call_pop(func, d, key, default=identity):
    """
    Return func(d.pop(key)) if key in d, else return default.
    """
    if key in d:
        return func(d.pop(key))
    return default


def getattri(o, attr):
    return getattr(o, attr, identity)


def getattrsi(o, *attrs):
    return reduce(lambda a, b: getattr(a, b, identity), attrs, o)
