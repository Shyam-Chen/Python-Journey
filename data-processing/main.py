from pathlib import Path
import polars as pl


# ========== 1. 建立 DataFrame ==========
df = pl.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "age": [25, 30, 35, 28, 32],
        "city": ["New York", "London", "Paris", "Tokyo", "Berlin"],
        "salary": [50000, 60000, 75000, 55000, 70000],
    }
)

print("原始資料:")
print(df)
# ┌─────────┬─────┬──────────┬────────┐
# │ name    ┆ age ┆ city     ┆ salary │
# │ ---     ┆ --- ┆ ---      ┆ ---    │
# │ str     ┆ i64 ┆ str      ┆ i64    │
# ╞═════════╪═════╪══════════╪════════╡
# │ Alice   ┆ 25  ┆ New York ┆ 50000  │
# │ Bob     ┆ 30  ┆ London   ┆ 60000  │
# │ Charlie ┆ 35  ┆ Paris    ┆ 75000  │
# │ David   ┆ 28  ┆ Tokyo    ┆ 55000  │
# │ Eve     ┆ 32  ┆ Berlin   ┆ 70000  │
# └─────────┴─────┴──────────┴────────┘


# ========== 2. 篩選與排序 ==========
filtered = df.filter(pl.col("age") > 28).sort("salary", descending=True)
print("\n年齡 > 28，按薪資降序:")
print(filtered)
# ┌─────────┬─────┬────────┬────────┐
# │ name    ┆ age ┆ city   ┆ salary │
# │ ---     ┆ --- ┆ ---    ┆ ---    │
# │ str     ┆ i64 ┆ str    ┆ i64    │
# ╞═════════╪═════╪════════╪════════╡
# │ Charlie ┆ 35  ┆ Paris  ┆ 75000  │
# │ Eve     ┆ 32  ┆ Berlin ┆ 70000  │
# │ Bob     ┆ 30  ┆ London ┆ 60000  │
# └─────────┴─────┴────────┴────────┘


# ========== 3. 選擇與轉換欄位 ==========
transformed = df.select(
    [
        pl.col("name"),
        pl.col("age"),
        (pl.col("salary") * 1.1).alias("salary_after_raise"),  # 加薪 10%
    ]
)
print("\n加薪 10% 後:")
print(transformed)
# ┌─────────┬─────┬────────────────────┐
# │ name    ┆ age ┆ salary_after_raise │
# │ ---     ┆ --- ┆ ---                │
# │ str     ┆ i64 ┆ f64                │
# ╞═════════╪═════╪════════════════════╡
# │ Alice   ┆ 25  ┆ 55000.0            │
# │ Bob     ┆ 30  ┆ 66000.0            │
# │ Charlie ┆ 35  ┆ 82500.0            │
# │ David   ┆ 28  ┆ 60500.0            │
# │ Eve     ┆ 32  ┆ 77000.0            │
# └─────────┴─────┴────────────────────┘


# ========== 4. 分組聚合 ==========
# 先新增一個部門欄位
df = df.with_columns(
    pl.when(pl.col("age") < 30).then(pl.lit("Junior")).otherwise(pl.lit("Senior")).alias("level")
)

# 開始分組和聚合
grouped = df.group_by("level").agg(
    [pl.col("salary").mean().alias("avg_salary"), pl.col("name").count().alias("count")]
)
print("\n按職級分組:")
print(grouped)
# ┌────────┬──────────────┬───────┐
# │ level  ┆ avg_salary   ┆ count │
# │ ---    ┆ ---          ┆ ---   │
# │ str    ┆ f64          ┆ u32   │
# ╞════════╪══════════════╪═══════╡
# │ Junior ┆ 52500.0      ┆ 2     │
# │ Senior ┆ 68333.333333 ┆ 3     │
# └────────┴──────────────┴───────┘


# ========== 5. 鏈式操作 ==========
result = (
    df.filter(pl.col("salary") > 55000)
    .with_columns((pl.col("age") + 1).alias("age_next_year"))
    .select(["name", "age", "age_next_year", "salary"])
    .sort("salary")
)
print("\n鏈式操作結果:")
print(result)
# ┌─────────┬─────┬───────────────┬────────┐
# │ name    ┆ age ┆ age_next_year ┆ salary │
# │ ---     ┆ --- ┆ ---           ┆ ---    │
# │ str     ┆ i64 ┆ i64           ┆ i64    │
# ╞═════════╪═════╪═══════════════╪════════╡
# │ Bob     ┆ 30  ┆ 31            ┆ 60000  │
# │ Eve     ┆ 32  ┆ 33            ┆ 70000  │
# │ Charlie ┆ 35  ┆ 36            ┆ 75000  │
# └─────────┴─────┴───────────────┴────────┘


# ========== 6. 從 CSV 讀取與寫入 ==========
# 建立路徑物件
output_dir = Path("__marimo__")
output_dir.mkdir(exist_ok=True)
file_path = output_dir / "employees.csv"

# 寫入
df.write_csv(file_path)

# 讀取
df_from_csv = pl.read_csv(file_path)
print("\n從 CSV 讀取:")
print(df_from_csv)
# ┌─────────┬─────┬──────────┬────────┬────────┐
# │ name    ┆ age ┆ city     ┆ salary ┆ level  │
# │ ---     ┆ --- ┆ ---      ┆ ---    ┆ ---    │
# │ str     ┆ i64 ┆ str      ┆ i64    ┆ str    │
# ╞═════════╪═════╪══════════╪════════╪════════╡
# │ Alice   ┆ 25  ┆ New York ┆ 50000  ┆ Junior │
# │ Bob     ┆ 30  ┆ London   ┆ 60000  ┆ Senior │
# │ Charlie ┆ 35  ┆ Paris    ┆ 75000  ┆ Senior │
# │ David   ┆ 28  ┆ Tokyo    ┆ 55000  ┆ Junior │
# │ Eve     ┆ 32  ┆ Berlin   ┆ 70000  ┆ Senior │
# └─────────┴─────┴──────────┴────────┴────────┘
