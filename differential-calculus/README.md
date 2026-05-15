# 微分學 (Differential Calculus)

---

### 目錄 (Table of Contents)

1. ...
2. ...

---

微分 (Differentiation) 是求函數在某點的瞬間變化率 (斜率)，即導數 (Derivative)：

```math
f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}
```

對整個陣列計算數值導數：

```py
x = np.linspace(-3, 3, 300)  # x 軸: -3 ~ 3，共 300 點
y = x**4  # f(x) = x⁴

dy = np.gradient(y, x)  # 數值微分，dy/dx: f'(x) = 4x³

plt.figure(figsize=(8, 4))
```
