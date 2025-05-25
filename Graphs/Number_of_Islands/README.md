## Number of Islands
Link: https://leetcode.com/problems/number-of-islands/
Difficulty: Medium
Topic: Graph, DFS, BFS, Union Find
Content: 
- Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
- An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - *What is the input format?* 2D binary grid
  - *What defines an island?* Connected '1's horizontally or vertically
  - *Can the grid be empty?* No, minimum size is 1x1
  - *Is diagonal connection considered?* No, only horizontal and vertical
  - *What is the time/space complexity requirement?* Not specified, but should be efficient

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
  Output: 1
  ```

- **Edge Case:**
  ```python
  Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
  Output: 3
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Need to track visited cells
- Is a **Queue** helpful? Yes, for BFS
- Consider **DFS** for exploring islands
- Consider **BFS** for exploring islands
- Consider **Union Find** for connected components

**Example Thought Process:**
- Need to find connected components → Use DFS/BFS
- Need to avoid revisiting cells → Use visited set/matrix
- Need to explore all directions → Check 4 neighbors
- Need to count islands → Increment counter for each new island

## 🔑 Key Data Structure:
- Visited matrix: for tracking explored cells
- Queue/Stack: for BFS/DFS traversal
- Counter: for counting islands

---

## Plan (Pseudocode)

### Solution 1: DFS
```pseudo
Process:
    Initialize visited matrix and island count
    FOR each cell in grid:
        IF cell is land and not visited:
            Increment island count
            DFS to mark all connected land as visited
    RETURN island count

DFS:
    Mark current cell as visited
    FOR each neighbor (up, down, left, right):
        IF neighbor is land and not visited:
            DFS(neighbor)
```

### Solution 2: BFS
```pseudo
Process:
    Initialize visited matrix and island count
    FOR each cell in grid:
        IF cell is land and not visited:
            Increment island count
            BFS to mark all connected land as visited
    RETURN island count

BFS:
    Add current cell to queue
    WHILE queue not empty:
        Process current cell
        Add unvisited land neighbors to queue
```

---

## Review
- Carefully review your implementation by checking:
  - Correctness of island detection
  - Proper handling of grid boundaries
  - Proper marking of visited cells
  - Time and space complexity requirements

---

## Evaluate
### Solution 1: DFS
- Time Complexity: O(m * n)
  - Visit each cell once
- Space Complexity: O(m * n)
  - Visited matrix
  - Recursion stack

### Solution 2: BFS
- Time Complexity: O(m * n)
  - Visit each cell once
- Space Complexity: O(m * n)
  - Visited matrix
  - Queue

---

## Optimize
- Could use Union Find for better performance
- Could optimize memory usage by modifying grid in-place
- Could handle edge cases more efficiently

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?
