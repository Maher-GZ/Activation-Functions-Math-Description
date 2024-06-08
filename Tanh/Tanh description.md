# Tanh Activation Function

## Overview
The hyperbolic tangent function, commonly abbreviated as tanh, is a type of activation function used in artificial neural networks. It is particularly useful in models where the output is desired to be in the range [-1, 1].

## Function
The tanh function is defined as:

## Equation 
tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))


where:
- `e` is the base of the natural logarithm (Euler's number)
- `x` is the input value to the function

## Characteristics
- **Range**: The output of tanh function is bounded between -1 and 1.
- **Symmetry**: The function is symmetric around the origin (0, 0).
- **S-shaped curve**: Similar to the sigmoid function, tanh also exhibits an S-shaped curve.
- **Smoothness**: Tanh function is smooth and differentiable everywhere, making it suitable for gradient-based optimization algorithms like gradient descent.

## Usage
Tanh activation function is commonly used in the hidden layers of neural networks, especially in recurrent neural networks (RNNs) and Long Short-Term Memory networks (LSTMs). It is also used in feedforward neural networks for tasks such as classification and regression.

## Advantages
- **Zero-Centered**: The tanh function is zero-centered, meaning its output is centered around zero. This can aid in quicker convergence during the training process.
- **Gradient Preservation**: Unlike the sigmoid function, which squashes the input values between 0 and 1, tanh squashes the values between -1 and 1, resulting in gradients that are preserved to some extent during backpropagation.
- **Non-linear**: Tanh is a non-linear function, allowing neural networks to learn complex relationships in the data.

## Limitations
- **Vanishing Gradient**: Like the sigmoid function, tanh is also susceptible to the vanishing gradient problem, especially in deep neural networks. This can hinder the training process, particularly for networks with many layers.

## Implementation
Tanh activation function can be easily implemented in most programming languages using their respective mathematical libraries. Here's a simple Python implementation:

```python
# import numpy as np

# def tanh(x):
#    return np.tanh(x)
