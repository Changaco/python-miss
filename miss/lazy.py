# This file is part of a program licensed under the terms of the GNU Lesser
# General Public License version 3 (or at your option any later version)
# as published by the Free Software Foundation.
#
# If you have not received a copy of the GNU Lesser General Public License
# along with this file, see <http://www.gnu.org/licenses/>.


from .collections import UserDict
from .six import PY3


class lazy_attr(object):
    """A decorator for lazy attributes.

    >>> class A(object):
    ...     @lazy_attr
    ...     def a(self):
    ...         return ['a']
    >>> a = A()
    >>> assert a.a is a.a  # check that evaluation only occurs once
    >>> a.a
    ['a']
    """

    def __init__(self, func):
        self.__func = func
        self.__name__ = func.__name__
        self.__module__ = func.__module__
        self.__doc__ = func.__doc__
        self.__dict__.update(func.__dict__)

    def __get__(self, inst, owner):
        if inst is None:
            return self

        name = self.__name__
        if name.startswith('__') and not name.endswith('__'):
            name = '_%s%s' % (owner.__name__, name)

        value = self.__func(inst)
        setattr(inst, name, value)
        return value


class lazy(object):
    """A basic lambda wrapper.

    >>> a = lazy(lambda: 'foo')
    >>> a()
    'foo'
    >>> assert a() is a()
    """

    def __init__(self, func):
        self.func = func

    __call__ = lambda self: self.value

    @lazy_attr
    def value(self):
        v = self.func()
        self.func = None
        return v


class lazy_dict(UserDict):
    """A lazy dictionary.

    >>> d = lazy_dict(dict(a=lambda:'a'))
    >>> d.pop('a')
    'a'
    >>> d.lazy('b', lambda: 1)
    >>> d
    {'b': 1}
    """
    def __init__(self, lambdas_dict, *args, **kwargs):
        kwargs.update((k, lazy(v)) for k, v in lambdas_dict.items())
        UserDict.__init__(self, *args, **kwargs)
    def __getitem__(self, key):
        o = UserDict.__getitem__(self, key)
        if isinstance(o, lazy):
            o = self[key] = o.value
        return o
    def __repr__(self):
        return (
            '{'+
            ', '.join(repr(k)+': '+repr(v) for k, v in self.items())+
            '}'
        )
    def lazy(self, key, func):
        self[key] = lazy(func)
