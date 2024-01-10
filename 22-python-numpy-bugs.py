# 22 python numpy bugs

import numpy as np

a = np.random.randn(5) # creates a data structure
print(a)
print(a.shape)
print(a.T)
print(np.dot(a,a.T))

# do not use dot product with a matrix and a vector when a.shape is something of the form (5,) because this will introduce wierd bugs difficult to understand

#also, when we have  a single bracket matrix, is a column vector, when it has two brackets, it is a row vector

# [1 2 3 4 5] this is a row vector
# [[1 2 3 4 5]] this is a column vector
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]] this is the same vector but formateed

b = np.random.randn(5, 1)
print(b)
print(b.T)
print(np.dot(b, b.T))

# don't use these kind of arrays for implementations
# a = np.random.randn(5)

# instead, use column vectors
# a = np.random.randn(5, 1)

# if you have any doubt about the size of a vector, check the shape
# assert(a.shape == (5, 1)))
# then reshape the vector
# a = a.reshape((5, 1))