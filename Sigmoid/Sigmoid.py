import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))




# Example 

# Example input array
input_array = np.array([-3.0, -1.0, 0.0, 1.0, 3.0])

# Apply the sigmoid function
output_array = sigmoid(input_array)

print(output_array)
