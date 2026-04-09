# 安裝與導入

```sh
vu add numpy
```

```py
import numpy as np
print(np.__version__)
# 2.4.4
```

# 執行

```sh
uv run marimo edit
```

# 建立和初始

`ndarray` 陣列

np.array(), np.zeros(), np.ones(), np.empty()

屬性：shape, dtype, ndim, size

- shape 結構形狀
- dtype 資料型別
- ndim 維度數
- size 元素總數

型別：int32, float64, bool

```py
zeros_2d = np.zeros((3, 3))
print(zeros_2d)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]


ones_int = np.ones((3, 3), dtype=int)
print(ones_int)
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]


empty_2d = np.empty((3, 3))
print(empty_2d)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
```

# 索引和切片

# 向量化 (Vectorization)

```py
arr = np.array([1, 2, 3, 4, 5])

# 基本運算（全部向量化）
arr + 10      # [11 12 13 14 15]
arr * 2       # [ 2  4  6  8 10]
arr ** 2      # [ 1  4  9 16 25]
np.sqrt(arr)  # [1.   1.41 1.73 2.   2.24]
np.sin(arr)
np.exp(arr)
```

```py
arr = np.array([1, 5, 8, 3, 10])

arr > 5       # [False False  True False  True]
arr == 5      # [False  True False False False]
(arr > 3) & (arr < 9)  # [False  True  True False False]
```

```py
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b         # [5 7 9]
a * b         # [ 4 10 18]
np.dot(a, b)  # 32 (點積)
```

```py
# ❌ 迭代器
arr_i = np.arange(10)
result_i = []
for val in arr_i:
    if val % 2 == 0:
        result_i.append(val * 2)
    else:
        result_i.append(val * 10)
print(result_i)

# ✅ 向量化
arr_v = np.arange(10)
result_v = np.where(arr_v % 2 == 0, arr_v * 2, arr_v * 10)
print(result_v)
```

```py
# NumPy 標量在數值運算上與 Python int 相容
np_val = np.int64(10)
py_val = 10

print(np_val + 5)    # 15
print(py_val + 5)    # 15
print(np_val == py_val)  # True
```

# 廣播 (Broadcasting)
