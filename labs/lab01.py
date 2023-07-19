def twenty_twenty_three():
    """Come up with the most creative expression that evaluates 
    to 2023,using only numbers and the +, *, and - operators.
    (no call expressions)
    >>> twenty_twenty_three()
    2023
    """
    return (200 * 10) + (200 // 10) + (2 + 1)

def twenty_twenty_three():
    """Come up with the most creative expression that evaluates 
    to 2023,using call expressions
    >>> twenty_twenty_three()
    2023
    """
    from operator import add, mul, sub, floordiv
    return add(mul(200, 10), add(floordiv(200, 10), add(2, 1)))

from math import pi

def sphere_area(r):
    """ Area of a sphere with radius r."""
    return (4 * pi * r * r)


def sphere_volume(r):
    """ Volume of a sphere with radius r."""
    return ((4/3)* pi * r * r * r)

def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return temp < 60 or raining

def sumNaturals(n):
    """ Sum all the first n natural numbers.
    >>> sumNaturals(3) # 1 + 2 + 3 = 6
    6
    >>> sumNaturals(5) # 1 + 2 + 3 + 4 + 5 = 15
    15
    """
    return int(n * (n + 1) / 2)
