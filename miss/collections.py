# This file is part of a program licensed under the terms of the GNU Lesser
# General Public License version 3 (or at your option any later version)
# as published by the Free Software Foundation.
#
# If you have not received a copy of the GNU Lesser General Public License
# along with this file, see <http://www.gnu.org/licenses/>.

"""
This module is a version of collections consistent in both python 2 and 3.

It is only made of re-exports from builtin modules, with one exception. Unlike
the builtin UserDict, the one in this module derives from dict, which means that
existing code using `isintance(obj, dict)` won't break.
"""

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
