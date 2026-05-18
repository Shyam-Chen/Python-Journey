import matplotlib.pyplot as plt
import numpy as np
import polars as pl
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from skl2onnx import to_onnx


# ========== 1. 準備 2025 年訓練數據 ==========
data_2025 = pl.DataFrame(
    {
        "月份": range(1, 13),
        "工單數量": [69, 74, 120, 102, 102, 72, 72, 85, 86, 80, 86, 63],
        "專案數量": [2, 0, 1, 3, 2, 0, 1, 0, 7, 5, 2, 6],
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
        "專案數量": [0, 0, 0, 6, 15, 11, 0, 2, 0, 0, 0, 3],
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


# ========== 8. 匯出模型 ==========

# 轉換成 ONNX (只要傳入一筆樣本，讓它自動推斷輸入型別)
onx = to_onnx(model_lr, X[:1].to_numpy())

# 儲存成 .onnx 檔案
with open("model.onnx", "wb") as f:
    f.write(onx.SerializeToString())

print("✅ 模型已成功匯出為 model.onnx")
