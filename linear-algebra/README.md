# 線性代數 (Linear Algebra)

---

### 目錄 (Table of Contents)

1. ...
2. ...

---

```py
import numpy as np
import matplotlib.pyplot as plt
```

## 向量 (Vector)

向量是線性代數的基本單位，可視為有方向與大小的量。

```math
\vec{v} = \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix}
```

```py
# 建立向量
v = np.array([1, 2, 3])
w = np.array([4, 5, 6])

# 向量加法
print(v + w)  # [5 7 9]

# 純量乘法
print(3 * v)  # [3 6 9]

# 內積 (Dot Product)
print(np.dot(v, w))  # 1*4 + 2*5 + 3*6 = 32

# 向量長度（L2 範數）
print(np.linalg.norm(v))  # sqrt(1+4+9) ≈ 3.742
```

## 矩陣 (Matrix)

```math
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
```

```py
# 建立矩陣
A = np.array(
    [
        [1, 2],
        [3, 4],
    ]
)

B = np.array(
    [
        [5, 6],
        [7, 8],
    ]
)
```

## 行列式 (Determinant)

行列式代表矩陣對空間「縮放」的倍數。

```py
A = np.array([[1, 2], [3, 4]])

det = np.linalg.det(A)
print(det)  # 1*4 - 2*3 = -2.0
```

## 逆矩陣 (Inverse Matrix)

```py
A = np.array([[1, 2], [3, 4]])

A_inv = np.linalg.inv(A)
print(A_inv)

# 驗證
print(A @ A_inv)  # 接近單位矩陣
```

## 解線性方程組 (Solving Linear Systems)

```math
\begin{cases}
2x + y = 5 \\
x + 3y = 10
\end{cases}
```

```py
A = np.array([[2, 1], [1, 3]])
b = np.array([5, 10])

# 使用 numpy 直接求解 (相較之下，比用逆矩陣更穩定)
x = np.linalg.solve(A, b)
print(x)  # [1. 3.] → x=1, y=3

# 驗證
print(A @ x)  # [5. 10.]
```

## 特徵值與特徵向量 (Eigenvalues and Eigenvectors)

## 矩陣的秩 (Rank)

```py
A = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
)  # 線性相依（第三列 = 第一+第二列×某倍數）

print(np.linalg.matrix_rank(A))  # 2（非滿秩）
```
