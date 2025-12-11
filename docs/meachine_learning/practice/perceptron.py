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

# 通过调用机器学习库的模块来实现
# import numpy as np 
# from sklearn.linear_model import Perceptron    Perceptron是一个类模块
# import matplotlib.pyplot as plt
# X1 = np.random.randn(10, 2)/4 + np.array([1, 1])
# y1 = np.ones(10)
# X2 = np.random.randn(10, 2)/4 + np.array([0, 0])
# y2 = -np.ones(10)
# X_train = np.vstack((X1, X2))
# y_train = np.hstack((y1, y2))

# plt.grid((-1,2))
# plt.plot(X1[:10, 0], X1[:10, 1], 'ro')
# plt.plot(X2[:10, 0], X2[:10, 1], 'bo')

# clf = Perceptron(
#     max_iter=1000,
#     eta0=1.0,
#     random_state=42
# )

# clf.fit(X_train, y_train)

# print(clf.coef_)
# x_ans = np.linspace(-1, 2, 1000)
# y_ans = - (clf.coef_[0][0] * x_ans + clf.intercept_)/clf.coef_[0][1]
# plt.plot(x_ans, y_ans, 'k-')
# plt.show()