# 深度學習 (Deep Learning)

---

### 目錄 (Table of Contents)

1. ...
2. ...

---

啟用函式 (Activation Function)：

啟用函式是神經網路中的非線性轉換元件，用來決定神經元的輸出是否應該被「啟用」，使模型能夠學習複雜的非線性關係。若沒有啟用函式，無論網路有多少層，其行為等同於單一線性模型。

```py
import torch.nn as nn
```

| 函式           | 說明                                      | 數學表達                  |
| -------------- | ----------------------------------------- | ------------------------- |
| `nn.ReLU`      | 最常用，將負值歸零                        | `max(0, x)`               |
| `nn.Sigmoid`   | 輸出介於 0 ~ 1，常用於二元分類            | `1 / (1 + e⁻ˣ)`           |
| `nn.Tanh`      | 輸出介於 -1 ~ 1，中心化輸出               | `(eˣ - e⁻ˣ) / (eˣ + e⁻ˣ)` |
| `nn.Softmax`   | 多類別分類輸出層，輸出總和為 1            | `eˣⁱ / Σeˣʲ`              |
| `nn.LeakyReLU` | 改良版 ReLU，負值給予小斜率避免神經元死亡 | `max(αx, x)`              |
| `nn.GELU`      | Transformer 常用，平滑且帶機率性質        | —                         |

---

### 二元分類

用貸款審核為例解釋：

[loan_approval.py](./loan_approval.py)

---

```py
import torch
```

## 張量 (Tensor)

### 建立張量

建立純量 (Scalar)，維度為 0D：

```py
scalar = torch.tensor(5)
print(scalar)  # tensor(5)
```

建立向量 (Vector)，維度為 1D：

```py
vector = torch.tensor([1, 2, 3])
print(vector)  # tensor([1, 2, 3])
```

建立矩陣 (Matrix)，維度為 2D：

```py
matrix = torch.tensor([[1, 2], [3, 4]])
print(matrix)
# tensor([[1, 2],
#         [3, 4]])
```

```py
# 全零張量
zeros = torch.zeros(2, 3)
print(zeros)
# tensor([[0., 0., 0.],
#         [0., 0., 0.]])


# 全一張量
ones = torch.ones(2, 3)
print(ones)
# tensor([[1., 1., 1.],
#         [1., 1., 1.]])


# 隨機張量 - 均勻分佈 0 ~ 1
rand = torch.rand(3, 3)
print(rand)
# e.g.
# tensor([[0.6391, 0.3513, 0.5518],
#         [0.0821, 0.0381, 0.2683],
#         [0.9853, 0.0711, 0.3010]])


# 隨機張量 - 標準常態分佈
randn = torch.randn(3, 3)
print(randn)
# e.g.
# tensor([[-0.7582, -0.7284, -1.6968],
#         [-1.0942,  0.1511,  0.2795],
#         [ 1.1361,  0.9498, -1.5853]])


# 等差數列
arange = torch.arange(0, 10, 2)
print(arange)  # tensor([0, 2, 4, 6, 8])


# 從 numpy 轉換
np_arr = np.array([[1, 2], [3, 4]])
from_numpy = torch.from_numpy(np_arr)
print(from_numpy)
# tensor([[1, 2],
#         [3, 4]])
```

### 張量屬性

```py
t = torch.randn(2, 3)

print(t.shape)  # torch.Size([2, 3])  ← 形狀
print(t.dtype)  # torch.float32  ← 資料型態
print(t.device)  # cpu  ← 所在裝置
print(t.ndim)  # 2  ← 維度數
```

### 數值運算

```py
# 逐元素運算
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

print(a + b)  # tensor([5, 7, 9])


# 矩陣乘法

# 數學函式

# 聚合運算
```

### 形狀操作

```py

```

### 自動微分 (Autograd)

```py
# requires_grad=True 表示需要計算梯度
x = torch.tensor(3.0, requires_grad=True)

# 定義函數：y = x² + 2x + 1
y = x**2 + 2 * x + 1

# 反向傳播 (自動求導)
y.backward()

# dy/dx = 2x + 2 = 2*3 + 2 = 8
print(x.grad)  # tensor(8.)
```

```math
\frac{dy}{dx} = 2x + 2 \Big|_{x=3} = 8
```

## 轉換器 (Transformer)

### 模型架構

Transformer 由 Encoder (編碼器) 和 Decoder (解碼器) 組成：

```
輸入序列
   ↓
[Encoder (編碼器)]
  ├─ Multi-Head Self-Attention
  ├─ Add & Norm (殘差連接 + 層歸一化)
  ├─ Feed Forward Network (FFN)
  └─ Add & Norm
   ↓
[Decoder (解碼器)]
  ├─ Masked Multi-Head Self-Attention
  ├─ Add & Norm
  ├─ Cross-Attention（與 Encoder 輸出互動）
  ├─ Add & Norm
  ├─ Feed Forward Network (FFN)
  └─ Add & Norm
   ↓
輸出序列
```

---

線性回歸：

```sh
$ uv run linear_regression.py
```

---

```sh
uv add torch
```

---

電腦視覺 (Computer Vision)

```sh
uv add torchvision
```

圖像分類

---

自然語言處理 (NLP)

```sh
uv add transformers[torch]
```

文字分類
