from typing import List
import heapq

class Solution:
    def minCostConnectPoints_Prim(self, points: List[List[int]]) -> int:
        """
        Solution 1: Prim's Algorithm
        Time Complexity: O(E log V)
        Space Complexity: O(V + E)
        
        Approach:
        - brute: search for every dist between every two nodes, and choose the smallest one
        - build an adj for every nodes first
        - and using Prim's algorithm to use Visit Set and Cost MinHeap to travel every possible edges
        """
        N = len(points)
        adj = {i: [] for i in range(N)}
        
        # Build adjacency list with distances
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visit = set()  # remember which nodes that been visited
        minH = [[0, 0]]  # for choosing the smallest one edge
        
        while len(visit) < N:  # set the limitation to travel every single node
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        
        return res
    
    def minCostConnectPoints_Kruskal(self, points: List[List[int]]) -> int:
        """
        Solution 2: Kruskal's Algorithm
        Time Complexity: O(E log E)
        Space Complexity: O(V + E)
        """
        N = len(points)
        edges = []
        
        # Create list of all edges
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append([dist, i, j])
        
        # Sort edges by cost
        edges.sort()
        
        # Union-Find implementation
        parent = list(range(N))
        rank = [0] * N
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
            return True
        
        # Kruskal's algorithm
        res = 0
        edges_used = 0
        
        for cost, x, y in edges:
            if union(x, y):
                res += cost
                edges_used += 1
                if edges_used == N - 1:
                    break
        
        return res

# Test cases
def test_solutions():
    solution = Solution()
    
    # Test case 1: Simple case
    points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    expected1 = 20
    assert solution.minCostConnectPoints_Prim(points1) == expected1
    assert solution.minCostConnectPoints_Kruskal(points1) == expected1
    
    # Test case 2: Edge case
    points2 = [[3,12],[-2,5],[-4,1]]
    expected2 = 18
    assert solution.minCostConnectPoints_Prim(points2) == expected2
    assert solution.minCostConnectPoints_Kruskal(points2) == expected2
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solutions()
