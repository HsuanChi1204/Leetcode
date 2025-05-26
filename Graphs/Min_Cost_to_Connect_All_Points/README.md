## Min Cost to Connect All Points
Link: https://leetcode.com/problems/min-cost-to-connect-all-points/
Difficulty: Medium
Topic: Graph, Minimum Spanning Tree, Union Find

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - *What is the input format?* Array of points, where each point is [x, y]
  - *Can the points be empty?* No, at least one point
  - *What is the cost between two points?* Manhattan distance
  - *What is the goal?* Connect all points with minimum total cost

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
  Output: 20
  Explanation: 
  - Connect [0,0] to [2,2] with cost 4
  - Connect [2,2] to [5,2] with cost 3
  - Connect [5,2] to [7,0] with cost 4
  - Connect [2,2] to [3,10] with cost 9
  Total cost = 20
  ```

- **Edge Case:**
  ```python
  Input: points = [[0,0]]
  Output: 0
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **Graph**? Yes, this is a Minimum Spanning Tree problem
- Is **Kruskal's Algorithm** helpful? Yes, for finding MST
- Consider **Union Find** for cycle detection
- Consider **Priority Queue** for edge selection

**Example Thought Process:**
- Need to connect all points → Minimum Spanning Tree
- Need to avoid cycles → Union Find
- Need to select minimum cost edges → Priority Queue
- Need to calculate distances → Manhattan distance

## 🔑 Key Data Structure:
- Union Find: for cycle detection
- Priority Queue: for edge selection
- Graph: for representing points and connections

---

## Plan (Pseudocode)

### Solution: Kruskal's Algorithm with Union Find
```pseudo
Process:
    Create Union Find data structure
    Calculate all possible edges and their costs
    Sort edges by cost
    Initialize total cost = 0
    FOR each edge in sorted edges:
        IF adding edge doesn't create cycle:
            Add edge to MST
            Add cost to total
            IF we have n-1 edges:
                BREAK
    RETURN total cost
```

---

## Review
- Carefully review your implementation by checking:
  - Correctness of MST construction
  - Proper handling of edge cases
  - Time and space complexity requirements

---

## Evaluate
### Solution: Kruskal's Algorithm
- Time Complexity: O(E log E)
  - E = number of edges = n(n-1)/2
  - Sorting edges takes O(E log E)
  - Union Find operations take O(log n)
- Space Complexity: O(E)
  - Store all edges
  - Union Find data structure

---

## Optimize
- Could use Prim's Algorithm instead
- Could optimize edge storage
- Could use more efficient Union Find implementation

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve? 