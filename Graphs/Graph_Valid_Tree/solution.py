from typing import List
from collections import defaultdict

class Solution:
    def validTree_dfs(self, n: int, edges: List[List[int]]) -> bool:
        """
        Solution 1: DFS Approach
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        if len(edges) != n - 1:  # A tree must have exactly n-1 edges
            return False
            
        # Create adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()
        
        def dfs(node: int, parent: int) -> bool:
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False  # Cycle detected
                if not dfs(neighbor, node):
                    return False
                    
            return True
        
        # Start DFS from node 0
        if not dfs(0, -1):
            return False
            
        # Check if all nodes are visited
        return len(visited) == n
    
    def validTree_union_find(self, n: int, edges: List[List[int]]) -> bool:
        """
        Solution 2: Union Find Approach
        Time Complexity: O(E * α(V))
        Space Complexity: O(V)
        """
        if len(edges) != n - 1:  # A tree must have exactly n-1 edges
            return False
            
        parent = list(range(n))
        rank = [0] * n
        
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> bool:
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return False  # Cycle detected
                
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
                
            return True
        
        # Process all edges
        for u, v in edges:
            if not union(u, v):
                return False
                
        return True

# Test cases
def test_solutions():
    solution = Solution()
    
    # Test case 1: Valid tree
    n1 = 5
    edges1 = [[0,1], [0,2], [0,3], [1,4]]
    expected1 = True
    assert solution.validTree_dfs(n1, edges1) == expected1
    assert solution.validTree_union_find(n1, edges1) == expected1
    
    # Test case 2: Invalid tree (cycle)
    n2 = 5
    edges2 = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    expected2 = False
    assert solution.validTree_dfs(n2, edges2) == expected2
    assert solution.validTree_union_find(n2, edges2) == expected2
    
    # Test case 3: Invalid tree (disconnected)
    n3 = 4
    edges3 = [[0,1], [2,3]]
    expected3 = False
    assert solution.validTree_dfs(n3, edges3) == expected3
    assert solution.validTree_union_find(n3, edges3) == expected3
    
    # Test case 4: Single node
    n4 = 1
    edges4 = []
    expected4 = True
    assert solution.validTree_dfs(n4, edges4) == expected4
    assert solution.validTree_union_find(n4, edges4) == expected4
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solutions()
