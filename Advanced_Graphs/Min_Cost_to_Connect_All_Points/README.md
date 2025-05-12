## Min Cost to Connect All Points
Link: https://leetcode.com/problems/min-cost-to-connect-all-points/
Difficulty: Medium
Topic: Graph, Minimum Spanning Tree, Prim's Algorithm, Kruskal's Algorithm
Content: 
- You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
- The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|.
- Return the minimum cost to make all points connected.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - *What is the input format?* Array of [x,y] coordinates
  - *What is the distance metric?* Manhattan distance
  - *Is the graph directed or undirected?* Undirected
  - *Can there be cycles in the MST?* No
  - *What if there are multiple valid MSTs?* Return the minimum cost one
  - *Is there any requirement on time/space complexity?* No
  - *Do you want me to write pseudocode first or just code the result out?* I'll write pseudocode first

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
  Output: 20
  ```

- **Edge Case:**
  ```python
  Input: points = [[3,12],[-2,5],[-4,1]]
  Output: 18
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Need to store graph structure.
- Is a **Dictionary** helpful? Yes, for adjacency list representation.
- Consider **Prim's Algorithm** for finding MST.
- Consider **Kruskal's Algorithm** for finding MST.
- Consider **Heap** for efficient edge selection.

**Example Thought Process:**
- Need to find minimum spanning tree → Prim's or Kruskal's
- Need to calculate distances → Manhattan distance
- Need to track visited nodes → Set
- Need to select minimum cost edges → Min Heap

## 🔑 Key Data Structure:
- Dictionary: for adjacency list representation
- Set: for tracking visited nodes
- Heap: for selecting minimum cost edges
- Union-Find: for Kruskal's algorithm

---

## Plan (Pseudocode)

### Solution 1: Prim's Algorithm
```pseudo
Process:
    Create adjacency list with distances
    Initialize visited set
    Initialize min heap with starting node
    Initialize total cost
    
    WHILE not all nodes visited:
        Get minimum cost edge from heap
        IF node not visited:
            Add cost to total
            Mark node as visited
            Add all unvisited neighbors to heap
    
    RETURN total cost
```

### Solution 2: Kruskal's Algorithm
```pseudo
Process:
    Create list of all edges with costs
    Sort edges by cost
    Initialize Union-Find structure
    Initialize total cost
    
    FOR each edge in sorted order:
        IF adding edge doesn't create cycle:
            Add edge to MST
            Add cost to total
    
    RETURN total cost
```

---

## Review
- Carefully review your implementation by checking:
  - Correctness of distance calculations
  - Proper handling of edge cases
  - Efficient use of data structures
  - Proper implementation of MST algorithms

---

## Evaluate
### Solution 1: Prim's Algorithm
- Time Complexity: O(E log V), where E is number of edges and V is number of vertices
  - Building adjacency list: O(V²)
  - Heap operations: O(E log V)
- Space Complexity: O(V + E)
  - O(V) for visited set
  - O(E) for adjacency list
  - O(V) for heap

### Solution 2: Kruskal's Algorithm
- Time Complexity: O(E log E)
  - Sorting edges: O(E log E)
  - Union-Find operations: O(E α(V))
- Space Complexity: O(V + E)
  - O(E) for edge list
  - O(V) for Union-Find structure

---

## Optimize
- Could use more efficient data structures for Union-Find
- Could implement path compression in Union-Find
- Could optimize edge generation process

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?
