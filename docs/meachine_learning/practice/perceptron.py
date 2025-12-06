import numpy as np 

# y belongs -1 or 1, x belongs vector, T is testset
def L(x, y, w, b):
    return y * (x @ w + b)

def faultset(T, w, b):
    new_set = []
    for item in T:
        if L(item.x, item.y, w, b) <= 0:
            new_set.append(item)
    
    return new_set

# 以二维点集为例
def perceptron(T):
    w = np.zeros(2)
    b = 0

    count = 0
    while count < 1000:
        count += 1
        fault_set = faultset(T, w, b)
        # 判断是否跳出
        if not fault_set:
            break

        for item in T:           
            if L(item.x, item.y, w, b) <= 0:
                w = w + item.y * item.x
                b = b + item.y
                break
        

    return w, b

class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y

X1 = np.random.randn(10, 2)/4 + np.array([1, 1])
y1 = np.ones(10)
X2 = np.random.randn(10, 2)/4 + np.array([0, 0])
y2 = -np.ones(10)
X = np.vstack((X1, X2))
y = np.hstack((y1, y2))

T = []
for i in range(20):
    data = Data(X[i], y[i])
    T.append(data)

w, b = perceptron(T)

import matplotlib.pyplot as plt

for item in T:
    plt.plot(item.x[0], item.x[1], 'ro' if (item.y > 0) else 'bo')
linex = np.linspace(-4, 4, 1000)
liney = (-w[0] * linex - b) / w[1]
plt.plot(linex, liney, '-', 'r')

plt.show()#
print(w)
print(b)