# 統計與機率 (Statistics and Probability)

---

### 目錄 (Table of Contents)

1. ...
2. ...

---

```py
import numpy as np
import polars as pl
import matplotlib.pyplot as plt
```

```sh
uv add scipy
```

```py
# 建立資料集
df = pl.DataFrame(
    {
        "score": [72, 85, 90, 60, 88, 95, 72, 78, 85, 92],
    }
)

# 計算描述統計
print(df.describe())

# 單獨計算各統計量
mean = df["score"].mean()
median = df["score"].median()
std = df["score"].std()
var = df["score"].var()
mode = df["score"].mode()

print(f"平均數 (Mean)    : {mean}")
print(f"中位數 (Median)  : {median}")
print(f"標準差 (Std Dev) : {std:.4f}")
print(f"變異數 (Variance): {var:.4f}")
print(f"眾數   (Mode)    : {mode.to_list()}")
```

## 二項分佈 (Binomial Distribution)

```py
from scipy.stats import binom
```

## 常態分佈 (Normal Distribution)

```py
from scipy.stats import norm
```
