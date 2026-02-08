# logistic regression

## logistic distribution

分布函数和密度函数如下所示：
```math
F(x) = \frac{1}{1 + \mathrm{e}^{-(x-\mu)/\gamma}}\\
f(x) = \frac{\mathrm{e}^{-(x - \mu)/\gamma}}{\gamma(1 + \mathrm{e}^{-(x - \mu)/\gamma})^2}
```

分布函数是关于$`(\mu, 0.5)`$中心对称的，类似于一个光滑的阶跃函数，$`\gamma`$表示了曲线在中兴两侧的增长速度，值越大，越近似于理想的阶跃函数。

## 二项逻辑回归模型

二项逻辑回归模型是一种二值分类模型，随机变量$`X`$取值为实数，$`Y`$的取值为0或1，通过监督学习的方式来估计模型参数。

```math
P(Y = 1|x) = \frac{\exp(\omega \cdot x + b)}{1 + \exp(\omega \cdot x + b)}\\
P(Y = 0|x) = \frac{1}{1 + \exp(\omega \cdot x + b)}
```

为了简化，我们可以将参数$`b`$也合到向量运算中，使$`\omega = (\omega^1, \omega^2, \cdots, \omega^n, b), x = (x^1, x^2, \cdots, x^n, 1)`$

可以通过极大似然估计法来估计模型的参数：对于训练集
```math
T = \{(x_1, y_1), (x_2, y_2), \cdots, (x_N, y_N)\}
```

令
```math
\frac{\exp(\omega \cdot x + b)}{1 + \exp(\omega \cdot x + b)} = p(x)
```
似然函数为
```math
L(\omega) = \prod_{i = 1}^N[p(x_i)]^{y_i}[1 - p(x_i)]^{1 - y_i}
```

对于该似然函数求最大值，可以通过梯度下降法或拟牛顿法得到最优解

## 多项逻辑回归

二类分类也可以推广为多类分类模型。若随机变量$`Y`$的取值为$`\{1, 2, 3, \cdots, K\}`$，可以这样定义分布函数
```math
P(Y = k|x) = \frac{\exp(\omega_k \cdot x)}{1 + \sum_{k = 1}^{K - 1}\exp(\omega_k \cdot x)},\quad k = 1, 2, \cdots, K - 1\\
P(Y = K|x) = \frac{1}{1 + \sum_{k = 1}^{K - 1}\exp(\omega_k \cdot x)}
```

可以类似地定义似然函数并进行最优化

# 最大熵模型

## 最大熵原理

最大熵原理认为，在概率模型的学习过程中，满足约束条件的结果中熵最大的模型被认为是最好的模型。

对于随机变量$`X`$，概率分布是$`P(X)`$，熵$`H(X) = -\sum_xP(x)\log P(x)`$，有下列不等式：
```math
0 \leq H(X) \leq \log|X|
```

由于这个等式当且仅当随机变量取均匀分布时成立，因此熵最大的结果也就是均匀分布的结果。

换一句话来说，熵最大原理也就是说**在满足约束条件的前提下，我们要尽可能地保留训练集中的不确定性，是不确定的部分是等可能的，已保留更多信息**

## 最大熵模型

分类模型实际上就是一个条件概率分布$`P(Y|X)`$，对于一个给定的数据集，可以确定联合分布与边缘分布的经验分布：
$$
\tilde{P}(X=x,Y=y) = \frac{v(X=x, Y=y)}{N}\\
\tilde{P}(X=x) = \frac{v(X=x)}{N}
$$

其中$`v(X=x, Y=y)`$表示样本中出现的频数