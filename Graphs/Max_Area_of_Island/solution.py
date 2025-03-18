# Solution 1: DFS
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 初步想法：
        # 剛剛找出島嶼數量，現在要比較哪個島嶼最大
        # 一樣用 dfs 進行島嶼計算，不過除了 island 以外，新增一個參數計算島嶼大小，最後 return 最大的數量

        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))
            # for dr, dc in directions:
            #     dfs(r + dr, c)
            #     dfs(r, c + dc)

        # forLoop to find the island start point
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))

        return res