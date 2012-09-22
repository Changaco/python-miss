# This file is part of a program licensed under the terms of the GNU Lesser
# General Public License version 3 (or at your option any later version)
# as published by the Free Software Foundation.
#
# If you have not received a copy of the GNU Lesser General Public License
# along with this file, see <http://www.gnu.org/licenses/>.


from .six.moves import reduce


inf = float('inf')
neg_inf = float('-inf')

def multiply(*xs):
    """
    >>> multiply(1, 2, 3)
    6
    """
    return reduce(lambda x, y: x*y, xs)
