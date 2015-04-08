#Numeric expression
print('Numeric expression')
print(2015)
print(2000+15)
print(1*2*((3*4*5//6)**3)+7+8)

#Call expression
print("\nCall expression")
print(max(2.0, 1.5))
print(pow(100,2))
print(pow(2,100))
print(max(1,-2,3,-4))
print(max(min(1,-2), min(pow(3,5),-4)))

#Importing and arithmetic with call expressions
print('\nImporting and arithmetic with call expressions')
from operator import add, mul
print(add(1,2))
print(mul(3,3))
print(add(2, mul(4,6)), add(3,5))
print(mul(10, add(mul(add(2,mul(4,6)), add(3,5)),-6.5)))

from math import sqrt
print(sqrt(169))

#Objects
print('\nObjects')
shakes = open('shakespeare.txt')
text = shakes.read().split()
print("Number of characters: ", len(text))
print("The first 15 characters: ", text[:15])
print("the: ", text.count('the'))
print("thou: ", text.count('thou'))
print("you: ", text.count('you'))
print("forsooth: ", text.count('forsooth'))
print(", : ", text.count(','))

#Sets
print('\nSets')
words = set(text)
print('length of words: ', len(words))
print('max order by letters in words: ', max(words))
print('max words with len as a key: ', max(words, key=len))

#Reversals
print('\nReversals')
print('The reversal of "draw" is: ', 'draw'[::-1])
print({w for w in words if w==w[::-1] and len(w)>4})
print({w for w in words if w[::-1] in words and len(w)==4})
print({w for w in words if w[::-1] in  words and len(w)>6})

