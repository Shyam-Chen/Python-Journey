import marimo

__generated_with = "0.22.4"
app = marimo.App()


@app.cell
def _():
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    return (arr,)


@app.cell
def _(arr):
    copied = arr.copy()
    viewed = arr.view()
    return copied, viewed


@app.cell
def _(arr, copied, viewed):
    arr[0] = 9

    print(f"arr    = {arr}")
    print(f"copied = {copied}")
    print(f"viewed = {viewed}")
    return


if __name__ == "__main__":
    app.run()
