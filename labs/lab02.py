def both_positive(x, y):
    """Returns True if both x and y are positive.
    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """

    return (x > 0) and (y > 0)

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a*a + b*b + c*c - min(a, b, c) * min(a, b, c)

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1,2,4,5,8,10,16,20,40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    factor = n - 1
    while factor > 0: 
        if n % factor == 0:  #check if n is divisible by the factor
            return factor #the case when yes
        factor -= 1 #the case when no, start again
    return None  #the case when no factors r found

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """

    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    step = 0 
    while n != 1:
        print(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = (n * 3 + 1)
        step += 1
    print(n)  
    return step + 1

def fibonacciN(n):
    """Return the nth Fibonacci number.
    Fibonacci Numbers is a series of numbers in which each number is the sum of the two preceding numbers

    >>> fibonacciN(5) # 1, 1, 2, 3, 5
    5
    >>> fibonacciN(7) 
    13

    """

    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1

    before, now = 1, 1 #start here (both first numbers r 1)
    count = 3 #need a way to keep track of my position in the seq.
    while count <= n:
        before, now = now, before + now #update the before valute to now value and now to the sum of 
        count += 1

    return now

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    divideby = 3
    while divideby * divideby <= n: #check divisibility up to the square root of n
        if n % divideby == 0:
            return False #notprime
        divideby += 2

    return True
