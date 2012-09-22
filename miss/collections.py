# This file is part of a program licensed under the terms of the GNU Lesser
# General Public License version 3 (or at your option any later version)
# as published by the Free Software Foundation.
#
# If you have not received a copy of the GNU Lesser General Public License
# along with this file, see <http://www.gnu.org/licenses/>.


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
