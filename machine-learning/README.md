# 機器學習 (Machine Learning)

---

### 目錄 (Table of Contents)

1. 回歸
2. 分類

---

```sh
$ uv add scikit-learn
```

```sh
$ uv add catboost
```

#### 將訓練好的模型輸出成 ONNX (Open Neural Network Exchange, `.onnx`)

```sh
$ uv add skl2onnx
```

```py
from skl2onnx import to_onnx

model = <ESTIMATOR_OBJECT>
model.fit(X, y)

# 轉換成 ONNX (只要傳入一筆樣本，讓它自動推斷輸入型別)
onx = to_onnx(model, X[:1])  # pandas
onx = to_onnx(model_lr, X[:1].to_numpy())  # polars

# 儲存成 .onnx 檔
with open("model.onnx", "wb") as f:
    f.write(onx.SerializeToString())
```

載入已儲存 .onnx 檔的並預測：

```sh
$ uv add onnxruntime
```

```py
import onnxruntime as ort

inference_session = ort.InferenceSession("model.onnx", providers=["CPUExecutionProvider"])
outputs = inference_session.run(None, {"input": <INPUT_TENSOR>})
print(outputs)
```

跨平台執行 (Node.js v24+)：

```sh
$ pnpm add onnxruntime-node
```

```sh
$ node verify.ts
```

---

## 回歸

回歸評估指標：

```math
\text{真實值} = y_i \quad \text{預測值} = \hat{y}_i \quad \text{樣本數} = n
```

### 平均絕對誤差 MAE (Mean Absolute Error)

https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-error

- 誤差單位與目標變數相同
- 所有誤差等權重對待

```py
from sklearn.metrics import mean_absolute_error

print(f"MAE: {mean_absolute_error(y_true, y_pred):.4f}")
```

### 均方誤差 MSE (Mean Squared Error)

- 對大誤差加重懲罰

```py
from sklearn.metrics import mean_squared_error
```

### 均方根誤差 RMSE (Root Mean Squared Error)

- MSE 的開根號版本，單位還原與目標變數相同

```py
from sklearn.metrics import root_mean_squared_error
```

### 中位數絕對誤差 MedAE (Median Absolute Error)

- 用中位數取代平均數，對離群值最穩健
- 資料含大量雜訊或異常值時特別適用

```py
from sklearn.metrics import median_absolute_error
```

### 決定係數 R² Score

- 通用的指標，代表模型解釋變異的比例
- 數值範圍通常在 0 ~ 1 (越接近 1 越好)
- 為負數時，模型比平均值基準還差

```py
from sklearn.metrics import r2_score

print(f"R² Score: {r2_score(y_true, y_pred):.4f}")
```

## 線性回歸

## 支援向量機 (Support Vector Machines, SVMs)

### 情境：垃圾電子郵件過濾

📧 垃圾郵件

- 特徵 1：關鍵字頻率
- 特徵 2：連結數
- `y=0`：正常郵件
- `y=1`：垃圾郵件

```py
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 特徵對應
# X[:,0] = 特定關鍵字出現頻率 (如「免費」、「中獎」)
# X[:,1] = 郵件中連結數量
# y = 0 (正常郵件) / 1 (垃圾郵件)

# 建立虛擬資料集
X, y = make_classification(
    n_samples=200,  # 200 封信件
    n_features=2,  # 2 項指標
    n_redundant=0,
    random_state=42,
)

# 切分訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 建立 SVM 分類器 (線性核心)
model = svm.SVC(kernel="linear", C=1.0)
# 這裡使用線性核心，因：
#  - 兩類資料可用一條直線分開成 y=0 和 y=1
#  - 僅有兩個特徵數，平面上的 X 軸和 Y 軸

# 訓練模型
model.fit(X_train, y_train)

# 預測與評估
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# 建立網格
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300), np.linspace(y_min, y_max, 300))

# 預測每個網格點
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 繪圖
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "PingFang TC", "Noto Sans CJK TC"]
plt.rcParams["axes.unicode_minus"] = False
plt.contourf(xx, yy, Z, alpha=0.3, cmap="coolwarm")
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolors="k")
plt.title("SVM 線性分類決策邊界")
plt.xlabel("特徵 1")
plt.ylabel("特徵 2")
plt.show()
```
