# 21 broadcasting

import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0], [1.2, 104.0, 52.0, 8.0],
              [1.8, 135.0, 99.0, 0.9]])

print(
    "calories for: apple, beef, eggs and potatos from carbs, protein and fat: "
)
print(A)

cal = A.sum(axis=0)
print("calories per food: " + str(cal))

percentage = 100 * A / cal.reshape(1, 4)
print(percentage)

# axios 0 is a column, while axis 1 is a row
# we added an A(3, 4) matrix to a calories matrix C(1, 4).
# the reshape function changes the matrix, so that i can be summed up.
