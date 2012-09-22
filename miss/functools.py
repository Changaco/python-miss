# This file is part of a program licensed under the terms of the GNU Lesser
# General Public License version 3 (or at your option any later version)
# as published by the Free Software Foundation.
#
# If you have not received a copy of the GNU Lesser General Public License
# along with this file, see <http://www.gnu.org/licenses/>.


def compose(f, g, unpack=False):
    """
    >>> compose(int, str)(0)
    0
    >>> compose(lambda *a: a, lambda *a: a, True)(0, 1)
    (0, 1)
    """
    if unpack:
        return lambda *args, **kwargs: f(*g(*args, **kwargs))
    else:
        return lambda *args, **kwargs: f(g(*args, **kwargs))
