#Imports
print('imports')
from math import pi, sin
print(pi*71/233)
print(sin(pi/2))

#Assignments
print('\nAssignments')
radius = 10
print(2*radius)
area, circ = pi*radius*radius, 2*pi*radius
print(area, circ)

#Function values
print('\nFunction values')
print(max)
print(max(3,4))
f=max
print(f)
print(f(3,4))
print(3,max)
f=2

#User-defined functions
print('\nUser-defined functions')
from operator import add,mul
print(add(2,3))
print(mul(2,3))

def square(x):
    return mul(x,x)

print(square(21))
print(square(add(2,5)))
print(square(square(3)))

def sum_squares(x,y):
    return add(square(x),square(y))

print(sum_squares(3,4))
print(sum_squares(5,12))

#Name conflicts
print('\nName confilcts, use the function name square as a argument')
def square(square):
    return mul(square, square)

print(square(4))

#Print
print('\nPrint function in python')
print(-2)
print('Go wolfpack!')
print(1,2,3)
print(None)
x = -2
x = print(-2)
print(x)
print(print(1), print(2))
