# This file is part of a program licensed under the terms of the GNU Lesser
# General Public License version 3 (or at your option any later version)
# as published by the Free Software Foundation.
#
# If you have not received a copy of the GNU Lesser General Public License
# along with this file, see <http://www.gnu.org/licenses/>.


from .identity import identity


class NS(object):
    """Namespace

    >>> ns = NS({'a': 0}, {'b': 0}, b=1)
    >>> ns
    NS({'a': 0, 'b': 1})
    >>> assert NS(['a', 'b'], 0, b=1) == ns
    >>> assert NS(ns) == ns
    >>> assert NS(ns) is not ns
    """
    def __init__(self, *args, **kwargs):
        if args:
            if isinstance(args[0], NS):
                for ns in args:
                    self.__dict__.update(ns.__dict__)
            elif isinstance(args[0], dict):
                for d in args:
                    self.__dict__.update(d)
            else:
                self.__dict__.update(dict.fromkeys(*args))
        if kwargs:
            self.__dict__.update(kwargs)
    def __contains__(self, item):
        return item in self.__dict__
    def __eq__(self, other):
        return self.__dict__ == other
    def __getitem__(self, key):
        return self.__dict__[key]
    def __iter__(self):
        return iter(self.__dict__)
    def __len__(self):
        return len(self.__dict__)
    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __repr__(self):
        return self.__class__.__name__+'('+repr(self.__dict__)+')'
    def __str__(self):
        return (
            self.__class__.__name__+
            '('+
            ', '.join(str(k)+'='+str(v) for k, v in self.__dict__.items())+
            ')'
        )
    def _clear(self):
        self.__dict__.clear()
    def _get(self, key, default=None):
        return self.__dict__.get(key, default)
    def _pop(self, *args, **kwargs):
        return self.__dict__.pop(*args, **kwargs)
    def _update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)
    def _setdefault(self, key, default):
        return self.__dict__.setdefault(key, default)


class iNS(NS):
    """Identity Namespace

    When accessing a nonexistent attribute, returns the Identity instead of
    raising an exception.
    """
    __getitem__ = __getattr__ = \
        lambda self, name: self.__dict__.get(name, identity)
    def __setattr__(self, key, value):
        if value != identity:
            self.__dict__[key] = value
    __setitem__ = __setattr__
    def _pop(self, key, default=identity):
        return self.__dict__.pop(key, default)
