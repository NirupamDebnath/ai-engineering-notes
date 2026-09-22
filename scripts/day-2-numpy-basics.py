#   • Task: Create a $5 \times 5$ matrix of random integers between 1 and 100.
#   • Challenge: Without using a loop, find the sum of each row and the mean of each column.

# learning docs:
# https://numpy.org/doc/stable/user/quickstart.html
# https://jalammar.github.io/visual-numpy/


import numpy as np

rand_matrix = np.random.randint(1, 101, size=(5, 5))

print("Random Matrix:\n", rand_matrix)

row_sums = np.sum(rand_matrix, axis=1)
col_means = np.mean(rand_matrix, axis=0)

print("Sum of each row:", row_sums)
print("Mean of each column:", col_means)