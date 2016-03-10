
from .six.moves import reduce


inf = float('inf')
neg_inf = float('-inf')

def multiply(*xs):
    """
    >>> multiply(1, 2, 3)
    6
    """
    return reduce(lambda x, y: x*y, xs)
