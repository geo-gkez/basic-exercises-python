import numpy as np
import math


def l2_dist(a, b):
    result = ((a - b) * (a - b)).sum()
    result = result ** 0.5
    return result 
a = np.random.rand(20,20)
b = np.random.rand(20,20)
print(l2_dist(a,b))
print(l2_dist(a.T,b.T))
print(l2_dist(np.reshape(a,(20*20)),np.reshape(b,(20*20))))


a1 = np.random.rand(4)
a2 = np.random.rand(4, 1)
a3 = np.array([[1, 2, 3, 4]])
a4 = np.arange(1, 4, 1)
a5 = np.linspace(1 ,4, 4)

print(a1.shape)
print(a2.shape)
print(a3.shape)
print(a4.shape)
print(a5.shape)


old = np.array([[1, 1, 1], [1, 1, 1]])
new = old
new[0, :2] = 0

print(old)