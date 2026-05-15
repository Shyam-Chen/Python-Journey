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
    ## 變數 (Variables)
    """)
    return


@app.cell
def _():
    num = 10  # 整數
    name = "Alice"  # 字串
    pi = 3.14  # 浮點數
    is_ok = True  # 布林值

    # 單一前導底線
    # 表示「內部使用 (internal)」或「非公開 API」，是一種約定 (convention)
    _score = 100
    return


@app.cell
def _():
    val = 10  # x 是 int
    val = "Hello"  # x 變成 str
    val = 3.14  # x 變成 float

    print(type(val))  # <class 'float'>
    return


@app.cell
def _():
    # 同時賦值多個變數
    a, b, c = 1, 2, 3
    print(f"a = {a}, b = {b}, c = {c}")

    # 多個變數指向同一個值
    x = y = z = 0
    print(f"x = {x}, y = {y}, z = {z}")

    # 交換變數
    a, b = b, a
    print(f"a = {a}, b = {b}, c = {c}")
    return


@app.cell
def _():
    s = "global"  # 全域變數


    def my_fn():
        s = "local"  # 區域變數 (只在函式內有效)
        print(s)  # local


    my_fn()
    print(s)  # global
    return


@app.cell
def _():
    count = 0


    def add():
        global count  # 修改全域變數，使用 `global` 關鍵字
        count += 1


    add()
    print(count)  # 1
    return


if __name__ == "__main__":
    app.run()
