""" For Scalar """

def relu(x):
    return max(0, x)



""" For numpy Vectorization """

import numpy as np

def relu(x):
    return np.maximum(0, x)

# Example 

# Example input array
input_array = np.array([-3.0, -1.0, 0.0, 1.0, 3.0])

# Apply the ReLU function
output_array = relu(input_array)

print(output_array)
