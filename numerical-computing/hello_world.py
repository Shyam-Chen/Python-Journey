import marimo

__generated_with = "0.23.0"
app = marimo.App()


@app.cell
def _():
    import numpy as np
    print(np.__version__)
    return (np,)


@app.cell
def _(np):
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    return


@app.cell
def _(np):
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr_2d)
    return


@app.cell
def _(np):
    arr_3d = np.ones((2, 3, 4))
    print(arr_3d)
    return


@app.cell
def _(np):
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
    return


if __name__ == "__main__":
    app.run()
