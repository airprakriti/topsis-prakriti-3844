 
from topsis_prak_3844.topsis import topsis
import numpy as np

# Example input
matrix = np.array([[250, 16, 12, 5],
                   [200, 16, 8, 3],
                   [300, 32, 16, 4],
                   [275, 32, 8, 4],
                   [225, 16, 16, 2]])
weights = [0.25, 0.25, 0.25, 0.25]
impacts = ["+", "+", "-", "+"]

# Calculate scores
scores = topsis(matrix, weights, impacts)
print(scores)
