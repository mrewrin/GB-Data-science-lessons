from itertools import count
from math import factorial

def factorial_gen():
    for el in count(1):
        yield factorial(el)

x = 0
for n in factorial_gen():
    if x == 15:
        break
    else:
        x += 1
        print(f'Facrotial {x} = {n}')

# for el in fact (n)