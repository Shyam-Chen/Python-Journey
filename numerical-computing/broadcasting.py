import marimo

__generated_with = "0.23.0"
app = marimo.App()


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(np):
    a = np.array(
        [
            [10, 20, 30],
            [40, 50, 60],
            [70, 80, 90],
        ]
    )
    b = np.array([1, 2, 3])
    print(a + b)
    return


if __name__ == "__main__":
    app.run()
