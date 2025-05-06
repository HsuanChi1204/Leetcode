from collections import defaultdict
from typing import List

class Solution:
    def findItinerary_DFS(self, tickets: List[List[str]]) -> List[str]:
        """
        Solution 1: DFS Approach
        Time Complexity: O(E log E)
        Space Complexity: O(E)
        """
        # Create adjacency list
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        
        # Sort destinations for lexicographical order
        for src in graph:
            graph[src].sort()
        
        # Initialize result and used tickets tracking
        result = []
        used = set()
        
        def dfs(current: str) -> None:
            # Try all possible destinations
            while graph[current]:
                # Get the next destination
                next_dest = graph[current].pop(0)
                # Continue DFS
                dfs(next_dest)
            # Add current airport to result
            result.append(current)
        
        # Start DFS from JFK
        dfs("JFK")
        # Reverse result since we built it backwards
        return result[::-1]
    
    def findItinerary_Hierholzer(self, tickets: List[List[str]]) -> List[str]:
        """
        Solution 2: Hierholzer's Algorithm
        Time Complexity: O(E log E)
        Space Complexity: O(E)
        """
        # Create adjacency list
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        
        # Sort destinations for lexicographical order
        for src in graph:
            graph[src].sort()
        
        # Initialize result
        result = []
        
        def dfs(current: str) -> None:
            # Process all edges from current node
            while graph[current]:
                # Get and remove next destination
                next_dest = graph[current].pop(0)
                # Continue DFS
                dfs(next_dest)
            # Add current airport to result
            result.append(current)
        
        # Start DFS from JFK
        dfs("JFK")
        # Reverse result since we built it backwards
        return result[::-1]

# Test cases
def test_solutions():
    solution = Solution()
    
    # Test case 1: Simple path
    tickets1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    expected1 = ["JFK","MUC","LHR","SFO","SJC"]
    assert solution.findItinerary_DFS(tickets1) == expected1
    assert solution.findItinerary_Hierholzer(tickets1) == expected1
    
    # Test case 2: Cycle
    tickets2 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    expected2 = ["JFK","NRT","JFK","KUL"]
    assert solution.findItinerary_DFS(tickets2) == expected2
    assert solution.findItinerary_Hierholzer(tickets2) == expected2
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solutions() 