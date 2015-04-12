#Operators
from operator import add, mul
print(2+3)
print(add(2,3))
print(2+3*4+5)
print(add(add(2,mul(3,4)),5))
print((2+3)*(4+5))
print(mul(add(2,3),add(4,5)))

#Division
print('\nDivision')
print(2015//10)
print(2015/10)
print(2015%10)
from operator import truediv, floordiv, mod
print(floordiv(2015, 10))
print(truediv(2015,10))
print(mod(2015,10))

#Multiple return values
print('\nMultiple return values')
def divide_exact(n,d):
    return n//d, n%d
print(2015//10, 2015%10)
quotient, remainder = divide_exact(2015,10)
print(quotient, remainder)

#Docstrings, Doctests, &default arguments
def divide_exact(n,d):
    """Return the quotient and remainder of dividing n by d.
    
    >>> quotient, remainder = divide_exact(2015,10)
    >>> quotient
    201
    >>> remainder
    5
    """
    return n//d, n%d

#Default arguments
def increase(number, by=1):
    return number+by

#Conditional expressions
def absolute_value(x):
    """Return the absolute value of x
    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(3)
    3
    """
    if x < 0:
        return -x
    elif x==0:
        return 0
    else:
        return x

#Summation via while
print('\nWhile statement')
i,total = 0,0
while i<3:
    i=i+1
    total = total+i

print(total)
