import numpy as np

np.random.uniform (0, 1)

for i in range (0, 10):
    a = int(input())
    x = np.random.uniform (0, 36)
    if a > 36 or a < 0:
        print('Input error!')
    if a == 0:
        print('Green')
    if 1 <= a <= 10:
        if a % 2 == 0:
            print('Black')
        else:
            print('Red')
    if 11 <= a <= 18:
        if a % 2 == 0:
            print('Red')
        else:
            print('Black')
    if 19 <= a <= 28:
        if a % 2 == 0:
            print('Black')
        else:
            print('Red')
    if 29 <= a <= 36:
        if a % 2 == 0:
            print('Red')
        else:
            print('Black')
