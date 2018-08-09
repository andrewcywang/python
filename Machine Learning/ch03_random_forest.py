from sklearn import datasets
import numpy as np
from sklearn.preprocessing import StandardScaler
# 修改後的繪圖程式
from decisionregions import plot_decision_regions
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data[:, [2, 3]]            # 切片
y = iris.target

print('Class labels:', np.unique(y))# 印出類別標籤

from sklearn.model_selection import train_test_split

# 7/3 分割訓練樣本與測試樣本
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y)

# 印出個數
print('Labels counts in y:', np.bincount(y))
print('Labels counts in y_train:', np.bincount(y_train))
print('Labels counts in y_test:', np.bincount(y_test))

# Standardizing the features:
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# 與 Decision Tree 使用相同的 combined
X_combined = np.vstack((X_train, X_test))
y_combined = np.hstack((y_train, y_test))

# 演算法則
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(criterion='gini',
                                n_estimators=25, 
                                random_state=1,
                                n_jobs=2)
forest.fit(X_train, y_train)

plot_decision_regions(X_combined, y_combined, 
                      classifier=forest, test_idx=range(105, 150))

plt.xlabel('petal length [cm]')
plt.ylabel('petal width [cm]')
plt.legend(loc='upper left')
plt.tight_layout()
#plt.savefig('images/03_22.png', dpi=300)
plt.show()
