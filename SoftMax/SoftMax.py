import numpy as np

def softmax(x):
    exp_x =[]
    soft=[]
    for i in range(len(x)):
        exp_x.append(np.exp(x[i]))
    sum_exp_x = sum(exp_x)
    for i in range(len(x)):
        soft.append(exp_x[i] / sum_exp_x)
    return soft



# Example
x = np.array([2, 6, 8])
output = softmax(x)
print(output)
