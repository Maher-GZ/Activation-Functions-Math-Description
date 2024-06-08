# Leaky ReLU Activation Function

## Overview
The Leaky Rectified Linear Unit (Leaky ReLU) is a type of activation function used in artificial neural networks. It is similar to the standard ReLU function but allows a small, positive slope for negative inputs, preventing the "dying ReLU" problem.

## Function
The Leaky ReLU function is defined as follows:

f(x) = max(alpha*x, x)

where alpha is a very small number like (.001,.01)



## Characteristics
- **Range**: The output of the Leaky ReLU function is in the range (-∞, +∞).
- **Similarity to ReLU**: Leaky ReLU behaves like ReLU for positive inputs, maintaining the same advantages such as efficiency and non-saturation.
- **Prevents Dead Neurons**: The small slope for negative inputs prevents neurons from becoming completely inactive, addressing the "dying ReLU" problem.
- **Non-linearity**: Like ReLU, Leaky ReLU introduces non-linearity to the network, enabling it to learn complex relationships in the data.

## Usage
Leaky ReLU activation function is commonly used in hidden layers of neural networks, especially in deep learning models such as convolutional neural networks (CNNs) and deep feedforward networks (DNNs). It is particularly effective in models dealing with high-dimensional data where the "dying ReLU" problem may occur.

## Advantages
- **Prevents Dying ReLU**: Leaky ReLU prevents neurons from becoming completely inactive by allowing a small, positive slope for negative inputs.
- **Efficiency**: Leaky ReLU is computationally efficient to compute and differentiate, making it suitable for large-scale neural network architectures.
- **Non-saturation**: Like ReLU, Leaky ReLU does not saturate for positive inputs, which helps mitigate the vanishing gradient problem.

## Limitations
- **Hyperparameter Tuning**: The slope parameter \( \alpha \) needs to be manually tuned, which adds an extra hyperparameter to the model.
- **Not Zero-Centered**: Leaky ReLU outputs are not zero-centered, which can lead to issues with optimization in some cases.

## Implementation
Leaky ReLU activation function can be easily implemented in most programming languages using simple conditional statements. Here's a Python implementation:

#```python
#def leaky_relu(x, alpha=0.01):
#    return x if x > 0 else alpha * x
