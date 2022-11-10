import numpy as np

k = 0
n = 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
print(k, n, k/n)
p = 6 / 2**4
print(p)
c5_3 = 5*4*3*2 / (3*2*2)
p5_3 = c5_3 / 2**5
print(p5_3)