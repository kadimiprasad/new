import math


def logarithm(x):
    try:
        return math.log10(x)
    except ValueError:
        print 'enter positive Number'
    except TypeError:
        print 'enter int or float'


logarithm(100000)
logarithm(-100)
logarithm("100")