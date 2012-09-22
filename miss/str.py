# This file is part of a program licensed under the terms of the GNU Lesser
# General Public License version 3 (or at your option any later version)
# as published by the Free Software Foundation.
#
# If you have not received a copy of the GNU Lesser General Public License
# along with this file, see <http://www.gnu.org/licenses/>.


def pstrip(s, prefix):
    """Prefix strip

    >>> pstrip('foo_oof', 'foo_')
    'oof'
    >>> pstrip('baroof', 'foo_')
    'baroof'
    """
    i = len(prefix)
    if s[:i] == prefix:
        return s[i:]
    return s

def sstrip(s, suffix):
    """Suffix strip

    >>> sstrip('foo.oof', '.oof')
    'foo'
    >>> sstrip('baroof', '.oof')
    'baroof'
    """
    i = - len(suffix)
    if s[i:] == suffix:
        return s[:i]
    return s
