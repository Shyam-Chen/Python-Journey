import marimo

__generated_with = "0.22.4"
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


if __name__ == "__main__":
    app.run()
