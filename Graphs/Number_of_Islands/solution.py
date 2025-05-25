from typing import List
from collections import deque

class Solution:
    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        """
        Solution 1: DFS Approach
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_count = 0
        
        def dfs(r: int, c: int):
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == "0" or 
                (r, c) in visited):
                return
                
            visited.add((r, c))
            # Explore all four directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island_count += 1
                    dfs(r, c)
        
        return island_count
    
    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        """
        Solution 2: BFS Approach
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_count = 0
        
        def bfs(r: int, c: int):
            queue = deque([(r, c)])
            visited.add((r, c))
            
            while queue:
                row, col = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c] == "1" and 
                        (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island_count += 1
                    bfs(r, c)
        
        return island_count

# Test cases
def test_solutions():
    solution = Solution()
    
    # Test case 1: Single island
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    expected1 = 1
    assert solution.numIslands_dfs(grid1) == expected1
    assert solution.numIslands_bfs(grid1) == expected1
    
    # Test case 2: Multiple islands
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    expected2 = 3
    assert solution.numIslands_dfs(grid2) == expected2
    assert solution.numIslands_bfs(grid2) == expected2
    
    # Test case 3: Empty grid
    grid3 = []
    expected3 = 0
    assert solution.numIslands_dfs(grid3) == expected3
    assert solution.numIslands_bfs(grid3) == expected3
    
    # Test case 4: No islands
    grid4 = [["0","0"],["0","0"]]
    expected4 = 0
    assert solution.numIslands_dfs(grid4) == expected4
    assert solution.numIslands_bfs(grid4) == expected4
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solutions()
            
