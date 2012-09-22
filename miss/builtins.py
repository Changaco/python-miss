# This file is part of a program licensed under the terms of the GNU Lesser
# General Public License version 3 (or at your option any later version)
# as published by the Free Software Foundation.
#
# If you have not received a copy of the GNU Lesser General Public License
# along with this file, see <http://www.gnu.org/licenses/>.


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
