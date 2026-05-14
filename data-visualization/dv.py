import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import numpy as np
    import polars as pl
    import matplotlib.pyplot as plt

    return np, pl, plt


@app.cell
def _(np, pl):
    df = pl.DataFrame(
        {
            "x": np.random.rand(10),
            "y": np.random.rand(10),
        }
    )

    print(df)
    return (df,)


@app.cell
def _(df, plt):
    plt.scatter(df["x"], df["y"], marker="o", label="Circle")
    plt.scatter(df["x"] + 0.1, df["y"] + 0.1, marker="s", label="Square")

    plt.title("Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()

    plt.show()
    return


if __name__ == "__main__":
    app.run()
