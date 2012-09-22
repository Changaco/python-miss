# This file is part of a program licensed under the terms of the GNU Lesser
# General Public License version 3 (or at your option any later version)
# as published by the Free Software Foundation.
#
# If you have not received a copy of the GNU Lesser General Public License
# along with this file, see <http://www.gnu.org/licenses/>.


from datetime import *


def age(born):
    today = date.today()
    try: # February 29 issue
        anniversary = born.replace(year=today.year)
    except ValueError:
        anniversary = born.replace(year=today.year, day=1, month=3)
    if anniversary > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year
