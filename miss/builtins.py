from .six.moves import reduce


def getattrs(o, *attrs, **kwargs):
    if 'default' in kwargs:
        default = kwargs['default']
        return reduce(lambda a, b: getattr(a, b, default), attrs, o)
    else:
        return reduce(getattr, attrs, o)
