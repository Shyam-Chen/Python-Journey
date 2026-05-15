# 程式設計 (Programming)

---

### 目錄 (Table of Contents)

1. [起手式 (Getting Started)](#起手式-getting-started)
2. [註解 (Comments)](#註解-comments)
3. [變數 (Variables)](#變數-variables)
4. 輸出 (Output)
5. [資料型別 (Data Types)](#資料型別-data-types)
6. 函式 (Functions)
7. 控制流程 (Control Flow)
8. 類別 (Classes)
9. 模組 (Modules)
10. 例外處理 (Exceptions)
11. 數學 (Math)
12. [日期與時間 (Date and Time)](#日期與時間-date-and-time)
13. [正規表達式 (Regular Expression)](#正規表達式-regular-expression)
14. 檔案操作 (File Operations)
15. 非同步 (Asynchronous)
16. 套件管理器 (Package Manager)

---

## 起手式 (Getting Started)

- 在線上瀏覽：Open in molab
- 在本地瀏覽：`uv run marimo edit getting_started.py`
- 在 VS Code 內瀏覽：[getting_started.py](./getting_started.py)

## 註解 (Comments)

- 在線上瀏覽：Open in molab
- 在本地瀏覽：`uv run marimo edit comments.py`
- 在 VS Code 內瀏覽：[comments.py](./comments.py)

## 變數 (Variables)

- 在線上瀏覽：Open in molab
- 在本地瀏覽：`uv run marimo edit variables.py`
- 在 VS Code 內瀏覽：[variables.py](./variables.py)

## 資料型別 (Data Types)

- 在線上瀏覽：[Open in molab](https://molab.marimo.io/notebooks/nb_D8eKCLswLnzHm6o2NH35Ub)
- 在本地瀏覽：`uv run marimo edit data_types.py`
- 在 VS Code 內瀏覽：[data_types.py](./data_types.py)

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

```
