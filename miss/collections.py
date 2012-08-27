from collections import *

from .six import PY3

if PY3:
    class UserDict(UserDict, dict): pass
else:
    import UserDict as _UserDict
    class UserDict(_UserDict.DictMixin, dict):
        __contains__ = dict.__contains__
        __iter__ = dict.__iter__
    from UserList import *
    from UserString import *
