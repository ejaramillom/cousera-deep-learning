# 17 - vectorization

import numpy as np
import time

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(a)

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()

print("Vectorized version:" + str(1000 * (toc - tic)) + "ms")

c = 0
tic = time.time()

for i in range(1000000):
  c += a[i] * b[i]
toc = time.time()

print("c value: " + str(c))
print("For loop:" + str(1000 * (toc - tic)) + "ms")
