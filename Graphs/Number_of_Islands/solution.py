# Solution 1: DFS
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 初步想法：
        # 用 dfs 的方式找每個點或區域的四周是不是都是水
        # 如果都是水 => res + 1

        # 換個想法：
        # 找到有幾個連續 1 的 island（？
        # 因為必定最少會有一個 island
        # 只要 1 無法繼續連下去，就算是一個 island 結案並建立

        # Solution:
        # use forloop to find first island
        # when found an island, then use DFS to search the connected lands
        # while checking for connected lands, I will mark them as "0" to remember that I have count them.
         
        # 1. initialize directions, rows, cols, number of island
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        island = 0

        # 3. define dfs function
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                grid[r][c] == "0"):
                return # for those out of bound or 0s, return

            grid[r][c] = "0" # mark the connected 1s to 0s
            for dr, dc in directions: # keep searching different directions
                dfs(r + dr, c + dc)

        # 2.  forloop to all node in grid to find island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    island += 1
        
        return island
            
