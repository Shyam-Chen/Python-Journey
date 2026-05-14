import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 輸出 (Output)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1. 單一值
    """)
    return


@app.cell
def _():
    print("Hello, World!")
    print(123)
    print(3.14)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. 多個值
    """)
    return


@app.cell
def _():
    print("Name:", "Alice", "|", "Age:", 22)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. 自訂分隔符號
    """)
    return


@app.cell
def _():
    print("a", "b", "c", sep=" | ")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4. 格式化
    """)
    return


@app.cell
def _():
    name = "Alice"
    age = 22

    print(f"Name: {name}, Age: {age}")
    return


if __name__ == "__main__":
    app.run()
