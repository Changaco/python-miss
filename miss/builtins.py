# This file is part of a program licensed under the terms of the GNU Lesser
# General Public License version 3 (or at your option any later version)
# as published by the Free Software Foundation.
#
# If you have not received a copy of the GNU Lesser General Public License
# along with this file, see <http://www.gnu.org/licenses/>.


from .six.moves import reduce


def getattrs(o, *attrs, **kwargs):
    if 'default' in kwargs:
        default = kwargs['default']
        return reduce(lambda a, b: getattr(a, b, default), attrs, o)
    else:
        return reduce(getattr, attrs, o)
