# 演算法 (Algorithms)

---

### 目錄 (Table of Contents)

1. [陣列 (Array) / 字串 (String)](#陣列-array--字串-string)
2. [鏈結串列 (Linked List)]
3. [堆疊 (Stack)]
4. [佇列 (Queue)]
5. [雜湊表 (Hash Table)]
6. [二元樹 (Binary Tree)]
7. [二元搜尋樹 (Binary Search Tree)]
8. [平衡樹 (Balanced Tree, AVL / Red-Black Tree)]
9. [堆積 (Heap)]
10. [字典樹 (Trie)]
11. [圖 (Graph)]
12. [排序 (Sorting)]
13. [搜尋 (Searching)]
14. [分治 (Divide and Conquer)]
15. [回溯 (Backtracking)]
16. [動態規劃 (Dynamic Programming)]
17. [貪婪 (Greedy)]
18. [位元操作 (Bit Manipulation)]

---

## 陣列 (Array) / 字串 (String)

初始化陣列，使用內建的 `list` 來建立動態陣列：

```py
arr: list[int] = [1, 2, 3, 4, 5]
filled_arr: list[int] = [0] * 5

print(filled_arr)  # [0, 0, 0, 0, 0]


s = "Hello"
lst = list(s)

print(lst)  # ['H', 'e', 'l', 'l', 'o']
```

訪問元素：

```py
arr: list[int] = [1, 2, 3, 4, 5]

print(arr)  # [1, 2, 3, 4, 5]
print(arr[0])  # 1
print(arr[-1])  # 5
print(arr[1:4])  # [2, 3, 4]  ← 切片 (Slicing)


s = "Hello"

print(s[0])  # H
print(s[-1])  # o
print(s[1:4])  # ell  ← 切片 (Slicing)
```

插入元素：

```py
arr: list[int] = [1, 2, 3, 4, 5]
arr.append(6)
print(arr)  # [1, 2, 3, 4, 5, 6]

arr: list[int] = [1, 2, 3, 4, 5]
arr.insert(0, 99)
print(arr)  # [99, 1, 2, 3, 4, 5]

arr: list[int] = [1, 2, 3, 4, 5]
arr.extend([6, 7, 8, 9, 10])
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr: list[int] = [1, 2, 3, 4, 5]
new_arr = arr + [6, 7, 8, 9, 10]
print(new_arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

刪除元素：

```py
arr: list[int] = [1, 2, 3, 4, 5]
arr.remove(3)
print(arr)  # [1, 2, 4, 5]

arr: list[int] = [1, 2, 3, 4, 5]
val = arr.pop()  # 移除最後一個
print(f"val = {val}, arr = {arr}")  # val = 5, arr = [1, 2, 3, 4]

arr: list[int] = [1, 2, 3, 4, 5]
val = arr.pop(1)  # 移除 index 1
print(f"val = {val}, arr = {arr}")  # val = 2, arr = [1, 3, 4, 5]

arr: list[int] = [1, 2, 3, 4, 5]
del arr[0]  # 刪除 index 0
print(arr)  # [2, 3, 4, 5]

arr: list[int] = [1, 2, 3, 4, 5]
del arr[1:3]  # 刪除 index 1~2
print(arr)  # [1, 4, 5]

arr: list[int] = [1, 2, 3, 4, 5]
arr.clear()
print(arr)  # []
```

走訪陣列：

```py
arr: list[int] = [10, 20, 30, 40, 50]

for idx, val in enumerate(arr):
    print(f"index = {idx}, value = {val}")

# index = 0, value = 10
# index = 1, value = 20
# index = 2, value = 30
# index = 3, value = 40
# index = 4, value = 50
```

雙指標 (Two Pointers) 走訪：

```py
arr = [1, 2, 3, 4, 5]
left, right = 0, len(arr) - 1

while left <= right:
    print(f"left={arr[left]}, right={arr[right]}")
    left += 1
    right -= 1

# left = 1, right = 5
# left = 2, right = 4
# left = 3, right = 3
```

多陣列同步走訪：

```py
names = ["Alice", "Bob", "Carol"]
scores = [60, 70, 90]

for name, score in zip(names, scores):
    print(f"{name}：{score} 分")

# Alice：60 分
# Bob：70 分
# Carol：90 分
```

### 題型

#### 交替合併字串 (1768. Merge Strings Alternately)

給你兩個字串 `word1` 和 `word2`。請你從 `word1` 開始，透過交替加上字母來合併字串。如果一個字串比另一個字串長，就將多出來的字母追加到合併後字串的結尾。

回傳*合併後的字串*。

範例 1：

```coffee
輸入: word1 = "abc", word2 = "pqr"
輸出: "apbqcr"
說明: 字串合併情況如下所示:
word1: a   b   c
word2:   p   q   r
合併後: a p b q c r
```

範例 2：

```coffee
輸入: word1 = "ab", word2 = "pqrs"
輸出: "apbqrs"
說明: 注意，word2 比 word1 長，"rs" 需要追加到合併後字串的結尾。
word1: a   b
word2:   p   q   r   s
合併後: a p b q   r   s
```

範例 3：

```coffee
輸入: word1 = "abcd", word2 = "pq"
輸出: "apbqcd"
說明: 注意，word1 比 word2 長，"cd" 需要追加到合併後字串的結尾。
word1: a   b   c   d
word2:   p   q
合併後: a p b q c   d
```

##### 解題

```py
from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))


# ========== 測試 ==========
sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))  # "apbqcr"
print(sol.mergeAlternately("ab", "pqrs"))  # "apbqrs"
print(sol.mergeAlternately("abcd", "pq"))  # "apbqcd"
```

使用雙指標 (Two Pointers)：

```py
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result: list[str] = []

        # 雙指標：兩字串都未耗盡時，交替取字元
        while i < len(word1) and j < len(word2):
            result.append(word1[i])  # 先取 word1 的字元
            result.append(word2[j])  # 再取 word2 的字元
            i += 1
            j += 1

        # 附加剩餘部分（最多只有一個字串有剩餘）
        result.append(word1[i:])  # 若 word1 較長，附加其餘部分
        result.append(word2[j:])  # 若 word2 較長，附加其餘部分

        return "".join(result)


# ========== 測試 ==========
sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))  # "apbqcr"
print(sol.mergeAlternately("ab", "pqrs"))  # "apbqrs"
print(sol.mergeAlternately("abcd", "pq"))  # "apbqcd"
```

## 鏈結串列 (Linked List)
