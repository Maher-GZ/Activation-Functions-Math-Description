
# Sigmoid Activation Function

## Overview
The sigmoid function is a type of activation function used in artificial neural networks. It maps any real-valued number to the range between 0 and 1. It is particularly useful in models where the output is desired to be in the range [0, 1].

## Function
The sigmoid function, also known as the logistic function, is defined as:

sigma(x) = 1 \ (1 + e^{-x})


## Characteristics
- **Range**: The output of the sigmoid function is bounded between 0 and 1.
- **S-shaped curve**: Sigmoid function exhibits an S-shaped curve, similar to the cumulative distribution function of logistic distribution, hence its name "logistic function".
- **Smoothness**: Sigmoid function is smooth and differentiable everywhere, making it suitable for gradient-based optimization algorithms like gradient descent.

## Usage
Sigmoid activation function is commonly used in the hidden layers of neural networks, especially in binary classification tasks. It is also used in feedforward neural networks for tasks such as regression.

## Advantages
- **Output Interpretability**: Sigmoid outputs can be interpreted as probabilities, with values closer to 1 indicating higher confidence in the positive class.
- **Smooth Gradient**: Sigmoid function has a smooth gradient, allowing for efficient optimization during training.
- **Non-linear**: Sigmoid is a non-linear function, allowing neural networks to learn complex relationships in the data.

## Limitations
- **Vanishing Gradient**: Sigmoid function is susceptible to the vanishing gradient problem, especially in deep neural networks with many layers.
- **Not Zero-Centered**: Sigmoid outputs are not zero-centered, which may lead to slower convergence during training when combined with certain activation functions.

## Implementation
Sigmoid activation function can be easily implemented in most programming languages using their respective mathematical libraries. Here's a simple Python implementation:

```python
#import numpy as np

#def sigmoid(x):
    return 1 / (1 + np.exp(-x))
