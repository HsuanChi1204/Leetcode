# Union Find Solution


## ✨ Union-Find 是什麼？

Union-Find（並查集）是一種用來解決：
- 「集合合併」問題
- 「快速查詢兩個元素是否屬於同一集合」

在圖論問題中特別常見，尤其是：
- 判斷「兩個節點是否連通」
- 檢查「是否有環存在」
- 建立「最小生成樹」（Kruskal 演算法）


## ✨ 基本概念

Union-Find 結構通常包含兩個陣列：

| 名稱 | 說明 |
|:----|:----|
| `parent[i]` | 記錄節點 `i` 的父節點（或自己是自己的代表） |
| `rank[i]`（或 `size[i]`） | 記錄集合的大小或樹的高度（用於優化合併） |



## ✨ 兩個核心操作

### 1. `find(x)`
找到元素 `x` 所屬集合的代表元素（根節點）。

基本版：
```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 路徑壓縮：直接接到根節點
    return parent[x]
```

- **路徑壓縮（Path Compression）**：
  - 把搜尋過的節點直接連到根節點
  - 可以大幅降低後續查詢時間



### 2. `union(x, y)`
將元素 `x` 和 `y` 所屬的集合合併。

基本版：
```python
def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX == rootY:
        return False  # 已經在同一集合，不需要再合併

    # 以rank優化：小樹接到大樹
    if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
        rank[rootX] += rank[rootY]
    else:
        parent[rootX] = rootY
        rank[rootY] += rank[rootX]
    
    return True
```

- **以秩合併（Union by Rank）**：
  - 將小的集合併入大的集合
  - 保持樹的高度最小，提升效率



## ✨ 使用流程舉例

假設有 5 個節點，初始：
```
parent = [0, 1, 2, 3, 4]
rank = [1, 1, 1, 1, 1]
```

進行：
```python
union(0, 1)
union(1, 2)
union(3, 4)
```

結果：
- 0、1、2 在同一集合
- 3、4 在同一集合
- 5 個節點組成 2 個集合

---

## ✨ 為什麼 Union-Find 很快？

經過「路徑壓縮」+「以秩合併」後：
- 每次 `find` 與 `union` 的時間複雜度接近 **O(1)**！
- 實際時間複雜度是 **O(α(N))**，其中 α 是阿克曼函數的反函數，增長極慢，幾乎可視為常數。

---

## ✨ Union-Find 常見應用

| 題型 | 說明 |
|:----|:----|
| 連通性檢查 | 判斷兩個節點是否屬於同一集合 |
| 環檢查（Cycle Detection） | 加邊時如果兩節點已連通，說明有環出現 |
| 最小生成樹（MST）Kruskal | 在選邊時防止形成環 |
| 聯通子圖個數 | 數有多少獨立的集合 |

---

## ✨ 小練習：自己寫一個 Union-Find

```python
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += self.rank[rootX]
        return True
```

範例操作：
```python
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print(uf.find(2))  # 應該會回傳 0（路徑壓縮後）
print(uf.find(4))  # 4 還是自己一組
```


# 📝 總結

- Union-Find 用來處理集合管理、集合合併、連通性問題
- 兩大優化技巧：**路徑壓縮**、**以秩合併**
- 高效應對圖論中的「連通性」和「環檢查」
- 常見於：朋友圈問題、冗餘連線、最小生成樹（MST）等題目