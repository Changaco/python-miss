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
