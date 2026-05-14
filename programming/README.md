# 程式設計 (Programming)

---

### 目錄 (Table of Contents)

1. [環境設置](#環境設置)
2. [註解 (Comments)](#註解-comments)
3. [變數 (Variables)](#變數-variables)
4. 輸出 (Output)
5. [資料型別 (Data Types)](#資料型別-data-types)
6. 函式 (Functions)
7. 控制流程 (Control Flow)
8. 類別 (Classes)
9. 模組 (Modules)
10. ...
11. 數學 (Math)
12. [日期與時間](#日期與時間)
13. [正規表達式](#正規表達式)
14. 檔案操作 (File Operations)

---

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
$ uv add ruff --dev
```

```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["I"]
```

Lint:

```sh
$ uv run ruff check --fix
```

Format:

```sh
$ uv run ruff format
```

### 專案的依賴 (Dependencies)

新增依賴：

```sh
$ uv add <DEPENDENCY_NAME>

# 開發用
$ uv add <DEPENDENCY_NAME> --dev
```

同步依賴 (安裝依賴)：

```sh
$ uv sync

# 只同步正式環境用的依賴
$ uv sync --no-dev
```

### 專案 Python 版本

```sh
# 查看可用的 Python 版本
$ uv python list

# 安裝目標 Python 版本
$ uv python install 3.14

# 固定新版本到專案
$ uv python pin 3.14

# 重新同步環境
$ uv sync
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

## 資料型別 (Data Types)

```sh
$ uv run marimo edit data_types.py
```

## 日期與時間

`datetime` 是 Python 內建的標準模組，用來處理**日期**與**時間**相關操作。

日期：

```py
from datetime import date

# 建立指定日期
d = date(2024, 6, 12)
print(d)  # 2024-06-12

# 今天的日期
today = date.today()
print(today)  # e.g., 2026-03-15
```

時間：

```py
from datetime import time

# 建立指定時間
t = time(14, 30, 59)
print(t)  # 14:30:59
```

日期時間：

```py
from datetime import datetime

# 建立指定日期時間
dt = datetime(2024, 6, 12, 14, 30, 0)
print(dt)  # 2024-06-12 14:30:00

# 取得現在的日期時間
now = datetime.now()
print(now)  # e.g., 2026-03-15 14:30:09.473843
```

字串轉日期：

```py
from datetime import datetime

s = "2024-06-12 14:30:00"
dt = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")

print(type(dt))  # <class 'datetime.datetime'>
print(dt)  # 2024-06-12 14:30:00
```

ISO 8601 字串轉日期：

```py
from datetime import datetime

s = "2024-06-12T14:30:00.111Z"
dt = datetime.fromisoformat(s)

print(type(dt))  # <class 'datetime.datetime'
print(dt)  # 2024-06-12 14:30:00.111000+00:00
```

時間差：

```py
from datetime import datetime, timedelta

now = datetime.now()

# 加減時間
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
two_hours_later = now + timedelta(hours=2)
```

## 正規表達式

`re` 是 Python 內建的標準模組，用來進行字串的搜尋、比對、擷取與替換。

| 符號    | 意義                   | 範例                      |
| ------- | ---------------------- | ------------------------- |
| `.`     | 任意單一字元 (除換行)  | `a.c` → `abc`, `a1c`      |
| `\*`    | 前一字元出現 0 次以上  | `ab\*` → `a`, `ab`, `abb` |
| `+`     | 前一字元出現 1 次以上  | `ab+` → `ab`, `abb`       |
| `?`     | 前一字元出現 0 或 1 次 | `ab?` → `a`, `ab`         |
| `^`     | 字串開頭               | `^Hello`                  |
| `$`     | 字串結尾               | `world$`                  |
| `\d`    | 數字 `[0-9]`           | `\d+` → `123`             |
| `\w`    | 字母/數字/底線         | `\w+` → `abc_123`         |
| `\s`    | 空白字元               | `\s+`                     |
| `[]`    | 字元集合               | `[aeiou]`                 |
| `()`    | 群組擷取               | `(\d+)`                   |
| `{n,m}` | 出現 n 到 m 次         | `\d{2,4}`                 |

找出第一個匹配的，回傳 `str`：

```py
import re

result = re.search(r"\d+", "abc123def456")
print(result.group())  # 123
```

找出所有匹配的，回傳 `list`：

```py
import re

result = re.findall(r"\d+", "abc123def456")
print(result)  # ['123', '456']
```

取代匹配到的字串：

```py
import re

result = re.sub(r"\d+", "_", "abc123def456")
print(result)  # abc_def_

# 只取代前 n 個
result = re.sub(r"\d+", "_", "abc123def456", count=1)
print(result)  # abc_def456
```

預先編譯 (用於重複使用時)：

```py
import re

pattern = re.compile(r"\d+")

print(pattern.findall("abc123def456"))  # ['123', '456']
print(pattern.sub("_", "abc123def456"))  # abc_def_
```

## 檔案操作 (File Operations)

`open()`, `os`, `pathlib`, `glob`

```py

```
