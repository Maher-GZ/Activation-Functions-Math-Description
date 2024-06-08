""" For Scalar """

def leaky_relu(x, alpha=0.01):
    return x if x > 0 else alpha * x




""" For numpy Vectorization """

import numpy as np

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)


# Example 

# Example input array
input_array = np.array([-3.0, -1.0, 0.0, 1.0, 3.0])

# Apply the Leaky ReLU function
output_array = leaky_relu(input_array, alpha=0.01)

print(output_array)
