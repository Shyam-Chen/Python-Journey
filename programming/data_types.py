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
    ## 資料型別 (Data Types)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1. 數值 (Numeric)
    """)
    return


@app.cell
def _():
    a = 10  # int  ← 整數
    b = 3.14  # float  ← 浮點數
    c = 2 + 3j  # complex  ← 複數，用 j 標記虛數
    d = 1 + 1j

    print(type(a))  # <class 'int'>
    print(type(b))  # <class 'float'>
    print(type(c))  # <class 'complex'>
    print(c + d)  # (3+4j)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. 字串 (String)
    """)
    return


@app.cell
def _():
    s = "Hello, World!"

    print(type(s))  # <class 'str'>
    print(s)  # Hello, World!
    print(len(s))  # 13
    print(s.upper())  # HELLO, WORLD!
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. 布林值 (Boolean)
    """)
    return


@app.cell
def _():
    is_ok = True
    is_err = False

    print(type(is_ok))  # <class 'bool'>
    print(type(is_err))  # <class 'bool'>
    print(is_ok and is_err)  # False
    print(is_ok or is_err)  # True

    print(10 > 2)  # True
    print(10 < 2)  # False
    print(10 == 2)  # False
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4. 序列 (Sequence)
    """)
    return


@app.cell
def _():
    fruits = ["apple", "banana", "cherry"]

    point = (3, 4)

    r = range(0, 10, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 5. 字典 (Dictionary)
    """)
    return


@app.cell
def _():
    person = {
        "name": "Alice",
        "age": 22,
        "city": "Taipei",
    }

    print(person["name"])  # Alice

    person["age"] = 35  # 修改值
    person["job"] = "Engineer"  # 新增鍵和值
    print(person)  # {'name': 'Alice', 'age': 35, 'city': 'Taipei', 'job': 'Engineer'}
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 6. 集合 (Set)
    """)
    return


@app.cell
def _():
    n_s = {1, 2, 2, 2, 3}
    print(n_s)  # {1, 2, 3}  ← 自動去除重複的值

    a_s = {1, 2, 3}
    b_s = {2, 3, 4}
    print(a_s | b_s)  # {1, 2, 3, 4}  ← 聯集
    print(a_s & b_s)  # {2, 3}  ← 交集
    print(a_s - b_s)  # {1}  ← 差集
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 7. 空值 (None)
    """)
    return


@app.cell
def _():
    val = None
    print(type(val))  # <class 'NoneType'>

    if not val:
        print("val 為空的")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 8. 型別轉換 (Type Conversion)
    """)
    return


@app.cell
def _():
    x = "123"
    print(int(x))  # 123 (str → int)
    print(float(x))  # 123.0 (str → float)

    y = 3.99
    print(int(y))  # 3 (float → int，無條件捨去)

    z = 100
    print(str(z))  # "100" (int → str)
    print(bool(z))  # True (非 0 為 True)
    return


if __name__ == "__main__":
    app.run()
