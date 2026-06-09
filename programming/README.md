# 程式設計 (Programming)

---

### 目錄 (Table of Contents)

1. [起手式 (Getting Started)](#起手式-getting-started)
2. [註解 (Comments)](#註解-comments)
3. [變數 (Variables)](#變數-variables)
4. [輸出 (Output)](#輸出-output)
5. [資料型別 (Data Types)](#資料型別-data-types)
6. [型別提示 (Type Hints)](#型別提示-type-hints)
7. [函式 (Functions)](#函式-functions)
8. [控制流程 (Control Flow)](#控制流程-control-flow)
9. [類別 (Classes)](#類別-classes)
10. [模組 (Modules)](#模組-modules)
11. [例外處理 (Exception Handling)](#例外處理-exception-handling)
12. 數學 (Math)
13. [日期與時間 (Date and Time)](#日期與時間-date-and-time)
14. [正規表達式 (Regular Expression)](#正規表達式-regular-expression)
15. [檔案操作 (File Operations)](#檔案操作-file-operations)
16. [非同步 (Asynchronous)](#非同步-asynchronous)
17. [套件管理器 (Package Manager)](#套件管理器-package-manager)

---

## 起手式 (Getting Started)

- 在線上瀏覽：[Open in molab](https://molab.marimo.io/notebooks/nb_iEBpU8X1KhzBZde3n58gfZ)
- 在本地瀏覽：`uv run marimo edit getting_started.py`
- 在 VS Code 內瀏覽：[getting_started.py](./getting_started.py)

## 註解 (Comments)

- 在線上瀏覽：[Open in molab](https://molab.marimo.io/notebooks/nb_T5qtpSARdkCgHWquLVp1U7)
- 在本地瀏覽：`uv run marimo edit comments.py`
- 在 VS Code 內瀏覽：[comments.py](./comments.py)

## 變數 (Variables)

- 在線上瀏覽：[Open in molab](https://molab.marimo.io/notebooks/nb_Wm2Dgx8SSbQKbKjvbHNUtG)
- 在本地瀏覽：`uv run marimo edit variables.py`
- 在 VS Code 內瀏覽：[variables.py](./variables.py)

## 輸出 (Output)

- 在線上瀏覽：[Open in molab](https://molab.marimo.io/notebooks/nb_E49wcQ5D75EzTro5SZVNCL)
- 在本地瀏覽：`uv run marimo edit output.py`
- 在 VS Code 內瀏覽：[output.py](./output.py)

## 資料型別 (Data Types)

- 在線上瀏覽：[Open in molab](https://molab.marimo.io/notebooks/nb_D8eKCLswLnzHm6o2NH35Ub)
- 在本地瀏覽：`uv run marimo edit data_types.py`
- 在 VS Code 內瀏覽：[data_types.py](./data_types.py)

## 型別提示 (Type Hints)

```sh
$ uv add ty --dev
```

```py
name: str = "Alice"
age: int = 30
is_active: bool = True
```

```py
def get_names() -> list[str]:
    return ["Alice", "Bob", "Carol"]


def get_user_ages() -> dict[str, int]:
    return {"Alice": 30, "Bob": 25, "Carol": 40}


def get_coordinates() -> tuple[float, float]:
    return (40.7128, -74.0060)
```

型別別名 (Type Alias)：

```py
type Age = int
age: Age = 30
```

```py
type Age = str
age: Age = 30
# ❌ error[invalid-assignment]: Object of type `Literal[30]` is not assignable to `Age`
```

聯合型別 (Union Types)：

```py
rate: int | str = 1
```

泛型 (Generics)：

```py
def first_element[T](items: list[T]) -> T:
    return items[0]


print(first_element([1, 2, 3]))  # 1
print(first_element(["Alice", "Bob", "Carol"]))  # Alice
```

## 函式 (Functions)

- 在線上瀏覽：[Open in molab](https://molab.marimo.io/notebooks/nb_nEAvcGtnCH7wZeESJRD7z7)
- 在本地瀏覽：`uv run marimo edit functions.py`
- 在 VS Code 內瀏覽：[functions.py](./functions.py)

## 控制流程 (Control Flow)

數學中的邏輯條件：

```py
a = 10
b = 10

if a == b:
    print("a 等於 b")
```

行內簡寫 `if...else` (三元運算子 (Ternary Operator))：

```py
age = 18
status = "已成年" if age >= 18 else "未成年"
print(status)
```

邏輯運算子 (Logical Operators)：`and`、`or`、`not`

`pass` 陳述句：

```py
a = 100
b = 20

if a > b:
    pass
```

### `for` 迴圈

```py
# 迭代 List
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for index, value in enumerate(fruits):
    print(f"{index}: {value}")
```

### `while` 迴圈

```py
count = 0

while count < 5:
    print(count)
    count += 1
```

`break` 陳述句：

```py

```

### `match` 模式匹配

```py

```

## 類別 (Classes)

初始化物件 `__init__`：

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice", 22)
bob = = Person("Bob", 35)
```

### 類別方法 (Class Methods)

當使用 `print() / str()` 時，`__str__`：

```py

```

除錯時，`__repr__`：

```py

```

### 繼承 (Inheritance)

```py

```

### 封裝 (Encapsulation)

```py
class MyWord:
    def __init__(self, foo, bar, baz):
        self.foo = foo  # 公開屬性
        self._bar = bar  # 受保護屬性
        self.__bar = bar  # 私有屬性
```

### 多型 (Polymorphism)

```py
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"面積：{shape.area()}")
# 面積：78.5
# 面積：24
```

## 模組 (Modules)

```coffee
.
├── main.py
├── fn
│   └── math.py
├── .python-version
├── pyproject.toml
└── uv.lock
```

```py
# fn/math.py
def add(a: int, b: int) -> int:
    return a + b
```

```py
# math.py
from fn.math import add

print(add(1, 2))
```

```sh
$ uv run main.py
```

建立 `src` 資料夾：

```coffee
.
├── src
│   ├── main.py
│   └── fn
│       └── math.py
├── .python-version
├── pyproject.toml
└── uv.lock
```

```sh
$ uv run ./src/main.py
```

## 例外處理 (Exception Handling)

```py
try:
    # 可能發生錯誤的程式碼
    result = 10 / 0
except ZeroDivisionError as e:
    # 捕捉特定例外
    print(f"捕捉到錯誤：{e}")
finally:
    # 無論如何都會執行 (常用於釋放資源)
    print("程式結束")
```

| 例外名稱            | 觸發情境                 |
| ------------------- | ------------------------ |
| `ValueError`        | 傳入值型別正確但值不合法 |
| `TypeError`         | 型別錯誤（如字串加整數） |
| `ZeroDivisionError` | 除以零                   |
| `IndexError`        | 串列索引超出範圍         |
| `KeyError`          | 字典中不存在的鍵         |
| `FileNotFoundError` | 開啟不存在的檔案         |
| `AttributeError`    | 物件無此屬性或方法       |
| `NameError`         | 使用未定義的變數         |
| `ImportError`       | 模組無法匯入             |
| `StopIteration`     | 迭代器沒有更多元素       |
| `OverflowError`     | 數值運算結果太大         |
| `RecursionError`    | 遞迴超出最大深度         |

```py
try:
    num = int("abc")  # 無法轉換
except ValueError as e:
    print(f"ValueError：{e}")
```

捕捉多個例外：

```py
try:
    x = int(input("輸入數字："))
    result = 10 / x
except ValueError:
    print("請輸入有效數字！")
except ZeroDivisionError:
    print("不能除以零！")
except (TypeError, NameError) as e:
    # 同時捕捉多種例外
    print(f"其他錯誤：{e}")
```

捕捉所有例外：

```py
try:
    # 某些操作
    pass
except Exception as e:
    # Exception 是大多數內建例外的父類別
    print(f"發生錯誤：{type(e).__name__} - {e}")
```

主動拋出例外 `raise`：

```py
def divide(a, b):
    if b == 0:
        raise ValueError("除數不能為零！")  # 主動拋出
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)
```

## 日期與時間 (Date and Time)

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

## 正規表達式 (Regular Expression)

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
with open("filename.txt", "r", encoding="utf-8") as f:
    content = f.read()
# 離開 with 區塊後，檔案自動關閉
```

```py
with open("example.txt", "r", encoding="utf-8") as f:
    # 一次讀取全部內容
    content = f.read()
    print(content)

    # 逐行迭代
    for line in f:
        print(line.strip())
```

### 寫入檔案

```py
with open("output.txt", "w", encoding="utf-8") as f:
    # 寫入單行
    f.write("Hello, Python!\n")

    # 寫入多行
    f.writelines(["第一行\n", "第二行\n"])
```

讀取 → 取代 → 寫回：

```py
replacements = {
    "蘋果": "Apple",
    "香蕉": "Banana",
    "橘子": "Orange",
}

with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()

for old, new in replacements.items():
    content = content.replace(old, new)

with open("example.txt", "w", encoding="utf-8") as f:
    f.write(content)
```

## 非同步 (Asynchronous)

```py
import asyncio

async def greet(name: str, delay: int):
    print(f"[{name}] 開始...")
    await asyncio.sleep(delay)  # 模擬 I/O 等待
    print(f"[{name}] 完成！")

async def main():
    # 兩個任務「並發」執行，不是依序等待
    await asyncio.gather(
        greet("Task A", 2),
        greet("Task B", 1),
    )

asyncio.run(main())
```

- 並發 (Concurrency)：多個任務「在時間上重疊」進行 (可以互相切換或交錯執行)，但不一定同時在同一瞬間執行。重點在「邏輯上同時有多個工作在進行」。
- 並行 (Parallelism)：多個任務「在物理上同時」執行 (例如在多個 CPU 核心上同時跑)。重點在「實際同時執行」。

## 套件管理器 (Package Manager)

### 升級專案用 Python 版本

```sh
$ uv python list
```

```sh
$ uv python install 3.15
```

```sh
$ uv python pin 3.15
```

```toml
# pyproject.toml
requires-python = ">=3.15"
```

```sh
$ uv sync
```
