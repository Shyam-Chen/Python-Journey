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

```

刪除元素：

```py

```

走訪陣列：

```py
arr: list[int] = [10, 20, 30, 40, 50]

for idx, val in enumerate(arr):
    print(f"index={idx}, value={val}")

# index=0, value=10
# index=1, value=20
# index=2, value=30
# index=3, value=40
# index=4, value=50
```

雙指標 (Two Pointers) 走訪：

```py
arr = [1, 2, 3, 4, 5]
left, right = 0, len(arr) - 1

while left <= right:
    print(f"left={arr[left]}, right={arr[right]}")
    left += 1
    right -= 1

# left=1, right=5
# left=2, right=4
# left=3, right=3
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
