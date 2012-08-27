from .six.moves import reduce


inf = float('inf')
neg_inf = float('-inf')

multiply = lambda *xs: reduce(lambda x, y: x*y, xs)
