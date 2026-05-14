import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 註解 (Comments)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##單行註解 `#`
    """)
    return


@app.cell
def _():
    # 這是一個單行註解
    print("Hello, World!")  # 這也是註解，寫在程式碼後面

    # x = 10  ← 這行程式碼被註解掉了，所以不會被執行
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 多行註解 (連續 `#`)
    """)
    return


@app.cell
def _():
    # 這是第一行註解
    # 這是第二行註解
    # 這是第三行註解
    print("多行註解")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 文件字串 `"\"\"..."\"\"`
    """)
    return


@app.cell
def _():
    def add(a, b):
        """
        這個函式用來計算兩數之和。

        參數:
            a: 第一個數字
            b: 第二個數字

        回傳:
            兩數相加的結果
        """
        return a + b


    # 可以用 help() 查看文件字串
    help(add)
    return


if __name__ == "__main__":
    app.run()
