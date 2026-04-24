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
        "工單數量": [120, 135, 145, 130, 140, 160, 155, 150, 165, 175, 180, 185],
        "總工時": [480, 540, 580, 520, 560, 640, 620, 600, 660, 700, 720, 740],
        "專案數量": [45, 50, 55, 48, 52, 60, 58, 55, 62, 65, 68, 70],
        "PDN項目數量": [15, 18, 20, 16, 18, 22, 20, 19, 23, 25, 26, 28],
        "CCT項目數量": [18, 20, 22, 19, 21, 24, 23, 22, 25, 26, 27, 28],
        "HSIO項目數量": [12, 12, 13, 13, 13, 14, 15, 14, 14, 14, 15, 14],
    }
)


# ========== 2. 特徵工程 ==========
# 增加時間特徵
data_2025["季度"] = (data_2025["月份"] - 1) // 3 + 1
data_2025["是否年底"] = (data_2025["月份"] >= 11).astype(int)

# 增加衍生特徵
data_2025["平均單項工時"] = data_2025["總工時"] / data_2025["工單數量"]
data_2025["專案密度"] = data_2025["專案數量"] / data_2025["月份"]  # 專案累積速度


# ========== 3. 準備特徵和目標變數 ==========
# 選擇重要特徵（可根據需求調整）
features = [
    "專案數量",
    "總工時",
    "PDN項目數量",
    "CCT項目數量",
    "HSIO項目數量",
    "月份",
    "季度",
    "是否年底",
    "平均單項工時",
]

X = data_2025[features]
y = data_2025["工單數量"]


# ========== 4. 訓練模型 ==========
# 方法 A: 線性迴歸
model_lr = LinearRegression()
model_lr.fit(X, y)

# 方法 B: 隨機森林
model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
model_rf.fit(X, y)


# ========== 5. 評估模型 ==========
y_pred_lr = model_lr.predict(X)
y_pred_rf = model_rf.predict(X)

print("=" * 50)
print("模型評估結果：")
print("=" * 50)
# 決定係數
print(f"線性迴歸 - R² 分數: {r2_score(y, y_pred_lr):.4f}")
print(f"隨機森林 - R² 分數: {r2_score(y, y_pred_rf):.4f}")
# 平均絕對誤差
print(f"線性迴歸 - MAE: {mean_absolute_error(y, y_pred_lr):.2f}")
print(f"隨機森林 - MAE: {mean_absolute_error(y, y_pred_rf):.2f}")


# ========== 6. 特徵重要性分析 ==========
feature_importance = pd.DataFrame(
    {"特徵": features, "重要性": model_rf.feature_importances_}
).sort_values("重要性", ascending=False)

print("\n" + "=" * 50)
print("隨機森林 - 特徵重要性排名：")
print("=" * 50)
print(feature_importance.to_string(index=False))


# ========== 7. 預測 2026 年 ==========
# 假設有 2026 年的專案數量數據（根據趨勢成長）
data_2026 = pd.DataFrame(
    {
        "月份": range(1, 13),
        "專案數量": [72, 75, 78, 70, 73, 80, 82, 78, 85, 88, 90, 95],
        "總工時": [760, 780, 800, 740, 770, 840, 860, 820, 890, 920, 940, 980],
        "PDN項目數量": [29, 30, 32, 28, 30, 34, 35, 33, 36, 38, 39, 41],
        "CCT項目數量": [29, 30, 31, 28, 29, 32, 33, 31, 34, 35, 36, 38],
        "HSIO項目數量": [14, 15, 15, 14, 14, 14, 14, 14, 15, 15, 15, 16],
    }
)

# 添加相同的特徵
data_2026["季度"] = (data_2026["月份"] - 1) // 3 + 1
data_2026["是否年底"] = (data_2026["月份"] >= 11).astype(int)

# 預估平均單項工時（可使用 2025 年平均值或趨勢）
avg_work_hours_per_order = data_2025["平均單項工時"].mean()
data_2026["平均單項工時"] = avg_work_hours_per_order

data_2026["專案密度"] = data_2026["專案數量"] / data_2026["月份"]

X_2026 = data_2026[features]

# 執行預測
data_2026["預測工單_線性迴歸"] = model_lr.predict(X_2026).round(0).astype(int)
data_2026["預測工單_隨機森林"] = model_rf.predict(X_2026).round(0).astype(int)

print("\n" + "=" * 50)
print("2026 年預測結果：")
print("=" * 50)
print(
    data_2026[
        [
            "月份",
            "專案數量",
            "總工時",
            "PDN項目數量",
            "CCT項目數量",
            "HSIO項目數量",
            "預測工單_線性迴歸",
            "預測工單_隨機森林",
        ]
    ].to_string(index=False)
)

# 統計年度總計
print("\n" + "=" * 50)
print("2026 年度總計預測：")
print("=" * 50)
print(f"線性迴歸預測總工單數: {data_2026['預測工單_線性迴歸'].sum()} 張")
print(f"隨機森林預測總工單數: {data_2026['預測工單_隨機森林'].sum()} 張")
print(f"2025 年實際總工單數: {data_2025['工單數量'].sum()} 張")


# ========== 8. 視覺化 ==========
# 中文字體設定
plt.rcParams["font.sans-serif"] = [
    "Microsoft JhengHei",
    "PingFang TC",
    "Noto Sans CJK TC",
]
plt.rcParams["axes.unicode_minus"] = False

# 單一工單預測圖
plt.figure(figsize=(12, 8))

# 繪製線條
line1 = plt.plot(data_2025["月份"], data_2025["工單數量"], "o-", label="2025實際", linewidth=2)
line2 = plt.plot(
    data_2026["月份"],
    data_2026["預測工單_線性迴歸"],
    "s--",
    label="2026預測(線性迴歸)",
    linewidth=2,
)
line3 = plt.plot(
    data_2026["月份"],
    data_2026["預測工單_隨機森林"],
    "^--",
    label="2026預測(隨機森林)",
    linewidth=2,
)

# 標示數值
for x, y in zip(data_2025["月份"], data_2025["工單數量"]):
    plt.text(x, y - 5, f"{int(y)}", ha="center", va="bottom", fontsize=9)

for x, y in zip(data_2026["月份"], data_2026["預測工單_線性迴歸"]):
    plt.text(x, y + 5, f"{int(y)}", ha="center", va="top", fontsize=9)

for x, y in zip(data_2026["月份"], data_2026["預測工單_隨機森林"]):
    plt.text(x, y + 5, f"{int(y)}", ha="center", va="top", fontsize=9)

plt.xlabel("月份")
plt.ylabel("工單數量")
plt.title("工單數量預測比較")
plt.legend()
plt.grid(True, alpha=0.3)


# 圖表 1: 工單預測比較
# fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# 子圖 1: 工單數量預測
# axes[0, 0].plot(data_2025["月份"], data_2025["工單數量"], "o-", label="2025實際", linewidth=2)
# axes[0, 0].plot(
#     data_2026["月份"],
#     data_2026["預測工單_線性迴歸"],
#     "s--",
#     label="2026預測(線性迴歸)",
#     linewidth=2,
# )
# axes[0, 0].plot(
#     data_2026["月份"],
#     data_2026["預測工單_隨機森林"],
#     "^--",
#     label="2026預測(隨機森林)",
#     linewidth=2,
# )
# axes[0, 0].set_xlabel("月份")
# axes[0, 0].set_ylabel("工單數量")
# axes[0, 0].set_title("工單數量預測比較")
# axes[0, 0].legend()
# axes[0, 0].grid(True, alpha=0.3)

# 子圖 2: 專案數量趨勢
# axes[0, 1].plot(data_2025["月份"], data_2025["專案數量"], "o-", label="2025", linewidth=2)
# axes[0, 1].plot(data_2026["月份"], data_2026["專案數量"], "s-", label="2026", linewidth=2)
# axes[0, 1].set_xlabel("月份")
# axes[0, 1].set_ylabel("專案數量")
# axes[0, 1].set_title("專案數量趨勢")
# axes[0, 1].legend()
# axes[0, 1].grid(True, alpha=0.3)

# 子圖 3: 各類型項目分布（2026）
# x_pos = data_2026["月份"]
# width = 0.25
# axes[1, 0].bar(x_pos - width, data_2026["PDN項目數量"], width, label="PDN", alpha=0.8)
# axes[1, 0].bar(x_pos, data_2026["CCT項目數量"], width, label="CCT", alpha=0.8)
# axes[1, 0].bar(x_pos + width, data_2026["HSIO項目數量"], width, label="HSIO", alpha=0.8)
# axes[1, 0].set_xlabel("月份")
# axes[1, 0].set_ylabel("項目數量")
# axes[1, 0].set_title("2026 年各類型項目分布")
# axes[1, 0].legend()
# axes[1, 0].grid(True, alpha=0.3, axis="y")

# 子圖 4: 特徵重要性
# axes[1, 1].barh(feature_importance["特徵"], feature_importance["重要性"])
# axes[1, 1].set_xlabel("重要性")
# axes[1, 1].set_title("隨機森林 - 特徵重要性")
# axes[1, 1].grid(True, alpha=0.3, axis="x")

plt.tight_layout()
plt.show()
