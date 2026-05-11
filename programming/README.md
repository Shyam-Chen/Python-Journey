# 程式設計 (Programming)

## 環境設置

### 安裝 UV

Windows：

```powershell
>_ winget install --id=astral-sh.uv  -e
```

macOS：

```sh
$ brew install uv
```

### 安裝 Python

```sh
$ uv python install 3.14
```

### 初始化專案

```sh
$ uv init <PROJECT_NAME>
$ cd <PROJECT_NAME>
```

### 安裝和編輯 Notebook

```sh
$ uv add marimo --dev
```

```sh
$ uv run marimo edit
```

### 安裝 Ruff

程式碼格式化 (Formatter) 和靜態分析 (Linter)

```sh
uv add ruff --dev
```

```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["I"]
```

Lint:

```sh
uv run ruff check --fix
```

Format:

```sh
uv run ruff format
```

## 註解 (Comments)

### 單行註解 `#`

```py
# 這是一個單行註解
print("Hello, World!")  # 這也是註解，寫在程式碼後面

# x = 10  ← 這行程式碼被註解掉了，所以不會被執行
```

### 多行註解 (連續 `#`)

```py
# 這是第一行註解
# 這是第二行註解
# 這是第三行註解
print("多行註解")
```

### 文件字串 `"""..."""`

```py
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
```

## 變數 (Variables)

```py
x = 10  # 整數
name = "Alice"  # 字串
pi = 3.14  # 浮點數
is_ok = True  # 布林值

# 單一前導底線
# 表示「內部使用 (internal)」或「非公開 API」，是一種約定 (convention)
_score = 100
```

```py
x = 10  # x 是 int
x = "Hello"  # x 變成 str
x = 3.14  # x 變成 float

print(type(x))  # <class 'float'>
```

```py
# 同時賦值多個變數
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# 多個變數指向同一個值
x = y = z = 0
print(f"x = {x}, y = {y}, z = {z}")

# 交換變數
a, b = b, a
print(f"a = {a}, b = {b}, c = {c}")
```

```py
x = "global"  # 全域變數


def my_fn():
    x = "local"  # 區域變數 (只在函式內有效)
    print(x)  # local


my_fn()
print(x)  # global
```

在函式內修改全域變數使用 `global` 關鍵字：

```py
count = 0


def add():
    global count
    count += 1


add()
print(count)  # 1
```

---

- `pathlib`：路徑處理
- `re`：正規表達式
- `datetime`：日期與時間
- `collections`：資料結構
- `asyncio`：非同步 I/O
