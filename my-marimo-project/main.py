import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt


# ========== 1. 準備 2025 年訓練數據 ==========
data_2025 = pd.DataFrame(
    {
        "月份": range(1, 13),
        "專案數量": [45, 50, 55, 48, 52, 60, 58, 55, 62, 65, 68, 70],
        "實際工單": [120, 135, 145, 130, 140, 160, 155, 150, 165, 175, 180, 185],
    }
)


# ========== 2. 特徵工程 ==========
# 增加時間特徵
data_2025["季度"] = (data_2025["月份"] - 1) // 3 + 1
data_2025["是否年底"] = (data_2025["月份"] >= 11).astype(int)
data_2025["累積專案"] = data_2025["專案數量"].cumsum()


# ========== 3. 準備特徵和目標變數 ==========
features = ["專案數量", "月份", "季度", "是否年底"]
X = data_2025[features]
y = data_2025["實際工單"]


# ========== 4. 訓練模型 ==========
# 方法 A: 線性迴歸
model_lr = LinearRegression()
model_lr.fit(X, y)


# 方法 B: 隨機森林
# model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
# model_rf.fit(X, y)


# ========== 5. 評估模型 ==========
y_pred_lr = model_lr.predict(X)
# y_pred_rf = model_rf.predict(X)

print("線性迴歸 - R² 分數:", r2_score(y, y_pred_lr))
# print("隨機森林 - R² 分數:", r2_score(y, y_pred_rf))


# ========== 6. 預測 2026 年 ==========
# 假設您有 2026 年的專案數量數據
data_2026 = pd.DataFrame(
    {
        "月份": range(1, 13),
        "專案數量": [72, 75, 78, 70, 73, 80, 82, 78, 85, 88, 90, 95],  # 您的實際數據
    }
)

# 添加相同的特徵
data_2026["季度"] = (data_2026["月份"] - 1) // 3 + 1
data_2026["是否年底"] = (data_2026["月份"] >= 11).astype(int)

X_2026 = data_2026[features]

# 執行預測
data_2026["預測工單"] = model_lr.predict(X_2026)
# data_2026["預測工單_森林"] = model_rf.predict(X_2026)

print("\n2026 年預測結果：")
print(data_2026[["月份", "專案數量", "預測工單"]])
# print(data_2026[["月份", "專案數量", "預測工單", "預測工單_森林"]])


# ========== 7. 視覺化 ==========
# 設定中文字體
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]  # 微軟正黑體（Windows）
plt.figure(figsize=(12, 6))
plt.plot(data_2025["月份"], data_2025["實際工單"], "o-", label="2025實際", linewidth=2)
plt.plot(data_2026["月份"], data_2026["預測工單"], "s--", label="2026預測", linewidth=2)
plt.xlabel("月份")
plt.ylabel("工單數量")
plt.title("工單執行預測")
plt.legend()
plt.grid(True)
plt.show()
