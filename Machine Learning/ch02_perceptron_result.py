import matplotlib.pyplot as plt
import numpy as np
import pandas as pd     # 先讀取資料 - Andrew
from perceptron import Perceptron
from showregions import plot_decision_regions

df = pd.read_csv('iris.data', header=None)
# select setosa and versicolor - 取前面100筆資料訓練
y = df.iloc[0:100, 4].values
# 改成 1, -1
y = np.where(y == 'Iris-setosa', -1, 1)
# extract sepal length and petal length - 為了視覺化只取兩個維度
X = df.iloc[0:100, [0, 2]].values

# plot data - 先畫出分布圖
plt.scatter(X[:50, 0], X[:50, 1],
            color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='blue', marker='x', label='versicolor')

plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()
# 感知器 - 建構子
ppn = Perceptron(eta=0.1, n_iter=10)
# 進行訓練
ppn.fit(X, y)
# 畫出收斂圖
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of updates')
plt.show()
# 畫出結果區域
plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()
