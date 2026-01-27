# import matplotlib
# matplotlib.use('Agg')

# from sklearn.tree import DecisionTreeRegressor, plot_tree
# import matplotlib.pyplot as plt

# # 回归树
# X = [[30], [40], [50], [60], [70]]
# y = [100, 120, 150, 180, 210]

# reg = DecisionTreeRegressor(max_depth=2)
# reg.fit(X, y)

# print(reg.predict([[48]]))

# plt.figure(figsize=(12, 6))
# plot_tree(
#     reg,
#     feature_names=['area'],
#     filled=True,
#     rounded=True
# )
# plt.savefig("CART.png")

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 使用经典 Iris 数据集
X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

tree_full = DecisionTreeClassifier(
    criterion="gini",
    random_state=42
)

tree_full.fit(X_train, y_train)

print("Train accuracy:", accuracy_score(y_train, tree_full.predict(X_train)))
print("Test accuracy:", accuracy_score(y_test, tree_full.predict(X_test)))

path = tree_full.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas = path.ccp_alphas
impurities = path.impurities

trees = []

for alpha in ccp_alphas:
    clf = DecisionTreeClassifier(
        criterion="gini",
        ccp_alpha=alpha,
        random_state=42
    )
    clf.fit(X_train, y_train)
    trees.append(clf)

train_acc = []
test_acc = []

for clf in trees:
    train_acc.append(accuracy_score(y_train, clf.predict(X_train)))
    test_acc.append(accuracy_score(y_test, clf.predict(X_test)))

best_idx = np.argmax(test_acc)
best_alpha = ccp_alphas[best_idx]

print("Best alpha:", best_alpha)
print("Best test accuracy:", test_acc[best_idx])

best_tree = DecisionTreeClassifier(
    criterion="gini",
    ccp_alpha=best_alpha,
    random_state=42
)

best_tree.fit(X_train, y_train)

print("Final test accuracy:",
      accuracy_score(y_test, best_tree.predict(X_test)))

# 好东西，可以人造数据进行测试
from sklearn.datasets import make_classification
X, y = make_classification(
    n_samples=120,      # 样本很少
    n_features=50,      # 特征很多
    n_informative=3,    # 真正有用的很少
    n_redundant=10,
    n_classes=2,
    flip_y=0.15,        # 15% 标签噪声
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

tree_full = DecisionTreeClassifier(
    random_state=42
)

tree_full.fit(X_train, y_train)

print("No pruning")
print("Train accuracy:", accuracy_score(y_train, tree_full.predict(X_train)))
print("Test accuracy:", accuracy_score(y_test, tree_full.predict(X_test)))
