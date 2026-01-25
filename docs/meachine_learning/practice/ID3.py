import math
from collections import Counter

dataset = [
    ['adolescence', 'no', 'no', 'OK', 'no'],
    ['adolescence', 'no', 'no', 'good', 'no'], 
    ['adolescence', 'yes', 'no', 'good', 'yes'], 
    ['adolescence', 'yes', 'yes', 'OK', 'yes'],
    ['adolescence', 'no', 'no', 'OK', 'no'],
    ['midage', 'no', 'no', 'OK', 'no'],
    ['midage', 'no', 'no', 'good', 'no'],
    ['midage', 'yes', 'yes', 'good', 'yes'],
    ['midage', 'no', 'yes', 'awsome', 'yes'],
    ['midage', 'no', 'yes', 'awsome', 'yes'],
    ['old', 'no', 'yes', 'awsome', 'yes'],
    ['old', 'no', 'yes', 'good', 'yes'],
    ['old', 'yes', 'no', 'good', 'yes'],
    ['old', 'yes', 'no', 'awsome', 'yes'],
    ['old', 'no', 'no', 'awsome', 'no']
]

labels =['age', 'job', 'house', 'credit']

def entropy(data):
    labels = [row[-1] for row in data]
    counts = Counter(labels)
    total = len(data)

    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent

def split_dataset(data, axis, value):
    result = []
    for row in data:
        if row[axis] == value:
            reduced = row[:axis] + row[axis+1:]
            result.append(reduced)
    return result

def choose_best_feature(data):
    base_entropy = entropy(data)
    feature_num = len(data[0]) - 1

    best_gain = -1
    best_feature = -1

    for i in range(feature_num):
        values = set(row[i] for row in data)
        new_entropy = 0

        for value in values:
            subset = split_dataset(data, i, value)
            prob = len(subset) / len(data)
            new_entropy += prob * entropy(subset)

        gain = base_entropy - new_entropy

        if gain > best_gain:
            best_gain = gain
            best_feature = i

    return best_feature

def majority_class(data):
    labels = [row[-1] for row in data]
    return Counter(labels).most_common(1)[0][0]

def build_tree(data, labels):
    class_list = [row[-1] for row in data]

    # 停止条件 1：全是同一类
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]

    # 停止条件 2：没有特征了
    if len(data[0]) == 1:
        return majority_class(data)

    best_feat = choose_best_feature(data)
    best_label = labels[best_feat]

    tree = {best_label: {}}

    feat_values = set(row[best_feat] for row in data)

    sub_labels = labels[:best_feat] + labels[best_feat+1:]

    for value in feat_values:
        subtree = build_tree(
            split_dataset(data, best_feat, value),
            sub_labels
        )
        tree[best_label][value] = subtree

    return tree

tree = build_tree(dataset, labels)
print(tree)

