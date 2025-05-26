from typing import List
import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

class Solution:
    def minCostConnectPoints_kruskal(self, points: List[List[int]]) -> int:
        """
        Solution 1: Kruskal's Algorithm with Union Find
        Time Complexity: O(E log E) where E is the number of edges
        Space Complexity: O(E)
        """
        n = len(points)
        if n <= 1:
            return 0
        
        # Calculate all possible edges and their costs
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))
        
        # Sort edges by cost
        edges.sort()
        
        # Initialize Union Find
        uf = UnionFind(n)
        
        # Build MST
        total_cost = 0
        edges_used = 0
        
        for cost, i, j in edges:
            if uf.union(i, j):
                total_cost += cost
                edges_used += 1
                if edges_used == n - 1:
                    break
        
        return total_cost

    def minCostConnectPoints_prim(self, points: List[List[int]]) -> int:
        """
        Solution 2: Prim's Algorithm
        Time Complexity: O(E log V) where E is the number of edges and V is the number of vertices
        Space Complexity: O(V + E)
        """
        n = len(points)
        if n <= 1:
            return 0
        
        # Build adjacency list
        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prim's Algorithm
        res = 0
        visit = set()  # Track visited nodes
        minH = [[0, 0]]  # [cost, node] format
        
        while len(visit) < n:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            
            # Add all unvisited neighbors to the heap
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        
        return res

# Test cases
def test_solutions():
    solution = Solution()
    
    # Test case 1: Example case
    points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    expected1 = 20
    assert solution.minCostConnectPoints_kruskal(points1) == expected1
    assert solution.minCostConnectPoints_prim(points1) == expected1
    
    # Test case 2: Single point
    points2 = [[0,0]]
    expected2 = 0
    assert solution.minCostConnectPoints_kruskal(points2) == expected2
    assert solution.minCostConnectPoints_prim(points2) == expected2
    
    # Test case 3: Two points
    points3 = [[0,0],[1,1]]
    expected3 = 2
    assert solution.minCostConnectPoints_kruskal(points3) == expected3
    assert solution.minCostConnectPoints_prim(points3) == expected3
    
    # Test case 4: Three points in a line
    points4 = [[0,0],[1,0],[2,0]]
    expected4 = 2
    assert solution.minCostConnectPoints_kruskal(points4) == expected4
    assert solution.minCostConnectPoints_prim(points4) == expected4
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solutions() 