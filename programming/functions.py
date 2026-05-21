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
    ## 函式 (Functions)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1. 定義與呼叫函式
    """)
    return


@app.cell
def _():
    # 定義函式
    def my_fn():
        print("Hello, World!")


    # 呼叫函式
    my_fn()  # Hello, World!
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. 參數類型
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 2-1. 位置參數 (Positional Arguments)
    """)
    return


@app.cell
def _():
    def add(a, b):
        print(f"a = {a}, b = {b}")


    add(1, 2)  # a = 1, b = 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 2-2. 預設參數 (Default Arguments)
    """)
    return


@app.cell
def _():
    def greet(name, greeting="Hello"):
        print(f"{greeting}, {name}!")


    greet("Alice")  # Hello, Alice!
    greet("Alice", "Hi")  # Hi, Alice!
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 2-3. 關鍵字參數 (Keyword Arguments)
    """)
    return


@app.cell
def _():
    def profile(name, age):
        print(f"{name} is {age} years old.")


    profile(age=18, name="Alice")  # Alice is 18 years old.  ← 參數的順序可不同
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 2-4. 多個位置參數
    """)
    return


@app.cell
def _():
    def total(*args):
        print(sum(args))


    total(1, 2, 3, 4)  # 10
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 2-5. 多個關鍵字參數
    """)
    return


@app.cell
def _():
    def detail(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")


    detail(name="Alice", age=18, city="Taipei")
    # name: Alice
    # age: 18
    # city: Taipei
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. 回傳值 `return`
    """)
    return


@app.cell
def _():
    def multiply(a, b):
        return a * b


    result = multiply(4, 5)
    print(result)  # 20


    def min_max(lst):
        return min(lst), max(lst)


    lo, hi = min_max([3, 1, 9, 5])
    print(f"min = {lo}, max = {hi}")  # min = 1, max = 9
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4. 匿名函式 `lambda`
    """)
    return


@app.cell
def _():
    square = lambda x: x**2
    print(square(5))  # 25


    nums = [3, 1, 4, 1, 5]
    sorted_nums = sorted(nums, key=lambda x: -x)
    print(sorted_nums)  # [5, 4, 3, 1, 1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 5. 作用域 (Scope)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 5-1. 本地作用域 (Local Scope)
    """)
    return


@app.cell
def _():
    def print_message():
        message = "Hello, World!"  # 本地變數
        print(message)


    print_message()  # ✅ Hello, World!
    # print(message)  # ❌ NameError: name 'message' is not defined  ← 無法讀取 `print_message` 函式內的 `message` 本地變數
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 5-2. 全域作用域 (Global Scope)
    """)
    return


@app.cell
def _():
    count_a = 0  # 全域變數
    count_b = 0  # 全域變數


    def increment():
        print(count_a)  # ✅ 可以讀取全域變數
        # count_a += 1  # ❌ UnboundLocalError: cannot access local variable 'count_a' where it is not associated with a value

        global count_b  # 宣告使用全域變數  ← 若要操作全域變數，需要使用 `global` 關鍵字
        count_b += 1


    increment()
    increment()
    print(f"count_a = {count_a}, count_b = {count_b}")  # count_a = 0, count_b = 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 5-3. 封閉作用域 (Enclosing Scope)
    """)
    return


@app.cell
def _():
    def outer():
        count = 0  # 封閉變數

        def inner():
            nonlocal count  # 宣告使用封閉變數
            count += 1
            print(count)

        inner()  # 1
        inner()  # 2


    outer()
    return


@app.cell
def _():
    x = "global"  # 全域變數


    def print_outer():
        x = "enclosing"  # 封閉變數

        def print_inner():
            x = "local"  # 本地變數
            print(x)  # ✅ local

        print_inner()
        print(x)  # ✅ enclosing


    print_outer()
    print(x)  # ✅ global
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 6. 閉包 (Closure)
    """)
    return


@app.cell
def _():
    def make_multiplier(n):
        def multiplier(x):
            return x * n  # 記住了 n

        return multiplier


    double = make_multiplier(2)
    triple = make_multiplier(3)

    print(double(5))  # 10
    print(triple(5))  # 15
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 7. 修飾器 (Decorator)
    """)
    return


@app.cell
def _():
    # 修飾器
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("執行前...")  # 前置邏輯
            result = func(*args, **kwargs)  # 呼叫原始函式
            print("執行後...")  # 後置邏輯
            return result

        return wrapper


    # 使用 `@` 語法糖
    @my_decorator
    def say_hello():
        print("Hello, World!")


    say_hello()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 8. 型別提示 (Type Hints)
    """)
    return


@app.cell
def _():
    def typed_add(a: int, b: int) -> int:
        return a + b


    print(typed_add(1, 2))
    # 3


    def typed_greet(name: str) -> None:
        print(f"Hello, {name}!")


    print(typed_greet("Alice"))
    # Hello, Alice!
    # None
    return


if __name__ == "__main__":
    app.run()
