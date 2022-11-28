import numpy as np

a = np.array(
    [[1, 2, 3, 3, 1],
    [6, 8, 11, 10, 7]]
).transpose()

mean_a = np.mean(a, axis = 0)

a_centered = a - mean_a

a_centered_sp = a_centered.T[0] @ a_centered.T[1]

print(np.cov(a.T)[0, 1])
