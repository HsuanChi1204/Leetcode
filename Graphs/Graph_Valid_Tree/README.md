## Graph Valid Tree
Link: https://leetcode.com/problems/graph-valid-tree/
Difficulty: Medium
Topic: Graph, DFS, BFS, Union Find
Content: 
- Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - *What is the input format?* Number of nodes and list of edges
  - *What defines a valid tree?* No cycles and all nodes are connected
  - *Can the graph be empty?* No, n >= 1
  - *Are the edges directed?* No, undirected
  - *What is the time/space complexity requirement?* Not specified, but should be efficient

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]
  Output: true
  ```

- **Edge Case:**
  ```python
  Input: n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
  Output: false
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Need to track visited nodes
- Is a **Queue** helpful? Yes, for BFS
- Consider **DFS** for cycle detection
- Consider **BFS** for cycle detection
- Consider **Union Find** for connected components

**Example Thought Process:**
- Need to detect cycles → Use DFS/BFS
- Need to check connectivity → Use Union Find
- Need to avoid revisiting nodes → Use visited set
- Need to track parent nodes → Use parent array/map

## 🔑 Key Data Structure:
- Adjacency list: for graph representation
- Visited set: for tracking explored nodes
- Parent map: for cycle detection
- Union Find: for connectivity check

---

## Plan (Pseudocode)

### Solution 1: DFS
```pseudo
Process:
    Create adjacency list
    Initialize visited set and parent map
    FOR each node:
        IF node not visited:
            IF DFS finds cycle:
                RETURN false
    RETURN true if all nodes visited

DFS:
    Mark current node as visited
    FOR each neighbor:
        IF neighbor is parent:
            Skip
        IF neighbor is visited:
            RETURN true (cycle found)
        IF DFS(neighbor) finds cycle:
            RETURN true
    RETURN false
```

### Solution 2: Union Find
```pseudo
Process:
    Initialize Union Find with n nodes
    FOR each edge:
        IF nodes already connected:
            RETURN false (cycle found)
        Union the nodes
    RETURN true if all nodes connected
```

---

## Review
- Carefully review your implementation by checking:
  - Correctness of cycle detection
  - Proper handling of connectivity
  - Proper tracking of visited nodes
  - Time and space complexity requirements

---

## Evaluate
### Solution 1: DFS
- Time Complexity: O(V + E)
  - Visit each node and edge once
- Space Complexity: O(V)
  - Visited set
  - Recursion stack

### Solution 2: Union Find
- Time Complexity: O(E * α(V))
  - α is the inverse Ackermann function
- Space Complexity: O(V)
  - Union Find data structure

---

## Optimize
- Could use BFS instead of DFS
- Could optimize memory usage
- Could handle edge cases more efficiently

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?
