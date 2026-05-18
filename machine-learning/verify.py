import onnxruntime as ort
import numpy as np
import polars as pl

# ========== 預測資料 ==========
data_2026 = pl.DataFrame(
    {
        "月份": range(1, 13),
        "專案數量": [0, 0, 0, 6, 15, 11, 0, 2, 0, 0, 0, 3],
    }
)

data_2026 = data_2026.with_columns((pl.col("專案數量") / pl.col("月份")).alias("專案密度"))
X_2026 = data_2026.select(["月份", "專案數量", "專案密度"])


# ========== 驗證模型 ==========
inference_session = ort.InferenceSession("model.onnx", providers=["CPUExecutionProvider"])
input_name = inference_session.get_inputs()[0].name

X_test = X_2026.to_numpy().astype(np.float64)
pred = inference_session.run(None, {input_name: X_test})[0]


# ========== 整理結果 ==========
data_2026 = data_2026.with_columns(
    pl.Series("預測工單_線性迴歸", pred.flatten().round(0).astype(int)),
)

print("=" * 50)
print("2026 年預測結果：")
print("=" * 50)
with pl.Config(tbl_rows=-1):
    print(data_2026.select(["月份", "專案數量", "預測工單_線性迴歸"]))
print("\n" + "=" * 50)
print("2026 年度總計預測：")
print("=" * 50)
print(f"線性迴歸預測總工單數: {data_2026['預測工單_線性迴歸'].sum()} 張")
