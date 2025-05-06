## Reconstruct Itinerary
Link: https://leetcode.com/problems/reconstruct-itinerary/
Difficulty: Hard
Topic: Graph, DFS, Eulerian Path
Content: 
- You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and arrival airports of one flight.
- Reconstruct the itinerary in order and return it.
- All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
- If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - *Is the graph directed or undirected?* Directed
  - *Can there be cycles in the graph?* Yes
  - *What if there are multiple valid paths?* Return the lexicographically smallest one
  - *Is there any requirement on time/space complexity?* No
  - *Can I use Python to solve the problem or are there any languages you prefer me to use?* Python is preferred
  - *Do you want me to write pseudocode first or just code the result out?* I'll write pseudocode first
- **Write down key rules clearly**: 
  - Directed graph
  - Must start from "JFK"
  - Return lexicographically smallest path
  - All tickets must be used

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
  Output: ["JFK","MUC","LHR","SFO","SJC"]
  ```

- **Edge Case:**
  ```python
  Input: tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
  Output: ["JFK","NRT","JFK","KUL"]
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Need to store graph structure.
- Is a **Dictionary** helpful? Yes, for adjacency list representation.
- Consider **DFS** for finding the path.
- Consider **Hierholzer's Algorithm** for finding Eulerian path.

**Example Thought Process:**
- Need to find a path that uses all edges → Eulerian Path
- Need to handle multiple edges → Adjacency List with sorted destinations
- Need to track used tickets → Remove used edges or use counter

## 🔑 Key Data Structure:
- Dictionary: for adjacency list representation
- List: for storing the result path
- Set/List: for tracking used tickets

---

## Plan (Pseudocode)

### Solution 1: DFS Approach
```pseudo
Process:
    Create adjacency list from tickets
    Sort destinations for each airport
    Initialize result list
    Initialize used tickets set
    
    DFS(current_airport):
        WHILE current_airport has unused tickets:
            Get next destination
            Mark ticket as used
            DFS(next_destination)
        Add current_airport to result
    
    DFS("JFK")
    RETURN reversed result
```

### Solution 2: Hierholzer's Algorithm
```pseudo
Process:
    Create adjacency list from tickets
    Sort destinations for each airport
    Initialize result list
    
    DFS(current_airport):
        WHILE current_airport has unused edges:
            Get and remove next destination
            DFS(next_destination)
        Add current_airport to result
    
    DFS("JFK")
    RETURN reversed result
```

---

## Review
- Carefully review your implementation by checking:
  - Correctness of graph representation
  - Proper handling of multiple edges
  - Lexicographical ordering
  - Edge cases (cycles, multiple valid paths)
  - Ticket usage tracking

---

## Evaluate
### Solution 1: DFS
- Time Complexity: O(E log E), where E is the number of edges
  - Sorting destinations takes O(E log E)
  - DFS traversal takes O(E)
- Space Complexity: O(E)
  - O(E) for adjacency list
  - O(E) for recursion stack
  - O(E) for used tickets tracking

### Solution 2: Hierholzer's Algorithm
- Time Complexity: O(E log E)
  - Sorting destinations takes O(E log E)
  - Algorithm traversal takes O(E)
- Space Complexity: O(E)
  - O(E) for adjacency list
  - O(E) for recursion stack

---

## Optimize
- Could use a more efficient data structure for tracking used tickets
- Could implement iterative DFS to avoid recursion stack
- Could use a different sorting approach for destinations

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve? 