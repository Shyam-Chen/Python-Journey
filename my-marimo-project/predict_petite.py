import polars as pl
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt


# ========== 資料讀取 ==========
# 讀取 CSV（第一列為欄名）
actual_df = pl.read_csv("actual.csv")
csv_2025_df = pl.read_csv("2025.csv")
csv_2026_df = pl.read_csv("2026.csv")

# .row(0) 回傳第一列的 tuple，再轉為整數列表
actual_values = [int(v) for v in actual_df.row(0)]
csv_2025_values = [int(v) for v in csv_2025_df.row(0)]
csv_2026_values = [int(v) for v in csv_2026_df.row(0)]


# ========== 1. 準備 2025 年訓練數據 ==========
data_2025 = pl.DataFrame(
    {
        "月份": range(1, 13),
        "工單數量": actual_values,
        "專案數量": csv_2025_values,
    }
)


# ========== 2. 特徵工程 ==========
# 增加衍生特徵
data_2025 = data_2025.with_columns((pl.col("專案數量") / pl.col("月份")).alias("專案密度"))


# ========== 3. 準備特徵和目標變數 ==========
# 選擇重要特徵
features = [
    "月份",
    "專案數量",
    "專案密度",
]

X = data_2025.select(features)
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
feature_importance = pl.DataFrame(
    {
        "特徵": features,
        "重要性": model_rf.feature_importances_,
    }
).sort("重要性", descending=True)

print("\n" + "=" * 50)
print("隨機森林 - 特徵重要性排名：")
print("=" * 50)
print(feature_importance)


# ========== 7. 預測 2026 年 ==========
data_2026 = pl.DataFrame(
    {
        "月份": range(1, 13),
        "專案數量": csv_2026_values,
    }
)

# 添加相同的特徵
data_2026 = data_2026.with_columns((pl.col("專案數量") / pl.col("月份")).alias("專案密度"))

X_2026 = data_2026.select(features)

# 執行預測
data_2026 = data_2026.with_columns(
    [
        pl.Series("預測工單_線性迴歸", model_lr.predict(X_2026).round(0).astype(int)),
        pl.Series("預測工單_隨機森林", model_rf.predict(X_2026).round(0).astype(int)),
    ]
)

print("\n" + "=" * 50)
print("2026 年預測結果：")
print("=" * 50)
with pl.Config(tbl_rows=-1):
    print(data_2026.select(["月份", "專案數量", "預測工單_線性迴歸", "預測工單_隨機森林"]))

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
line1 = plt.plot(
    data_2025["月份"],
    data_2025["工單數量"],
    "o-",
    label="2025實際",
    linewidth=2,
)
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

# 取得各線條顏色
color1 = line1[0].get_color()
color2 = line2[0].get_color()
color3 = line3[0].get_color()

# 標示數值（套用對應顏色）
for x, y in zip(data_2025["月份"], data_2025["工單數量"]):
    plt.text(x, y - 5, f"{int(y)}", ha="center", va="bottom", fontsize=9, color=color1)

for x, y in zip(data_2026["月份"], data_2026["預測工單_線性迴歸"]):
    plt.text(x, y + 5, f"{int(y)}", ha="center", va="top", fontsize=9, color=color2)

for x, y in zip(data_2026["月份"], data_2026["預測工單_隨機森林"]):
    plt.text(x, y + 5, f"{int(y)}", ha="center", va="top", fontsize=9, color=color3)

plt.xlabel("月份")
plt.ylabel("工單數量")
plt.title("工單數量預測比較")
plt.legend()
plt.grid(True, alpha=0.3)


plt.tight_layout()
plt.show()
