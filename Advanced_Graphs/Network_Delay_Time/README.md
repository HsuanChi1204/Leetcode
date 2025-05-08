## Network Delay Time
Link: https://leetcode.com/problems/network-delay-time/
Difficulty: Medium
Topic: Graph, Shortest Path
Content: 
- You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
- We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - *Is the graph directed or undirected?* Directed
  - *Can there be cycles in the graph?* Yes
  - *Can there be negative weights?* No
  - *What if some nodes are unreachable?* Return -1
  - *Is there any requirement on time/space complexity?* No
  - *Can I use Python to solve the problem or are there any languages you prefer me to use?* Python is preferred
  - *Do you want me to write pseudocode first or just code the result out?* I'll write pseudocode first
- **Write down key rules clearly**: 
  - Directed graph with positive weights
  - Need to find shortest path to all nodes
  - Return -1 if any node is unreachable

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
  Output: 2
  Explanation: The signal starts at node 2 and reaches all nodes in 2 units of time.
  ```

- **Edge Case:**
  ```python
  Input: times = [[1,2,1]], n = 2, k = 2
  Output: -1
  Explanation: Node 2 cannot receive the signal from node 1.
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Need to store graph structure.
- Is a **Dictionary** helpful? Yes, for adjacency list representation.
- Consider **Dijkstra's Algorithm** for finding shortest paths.
- Consider **Priority Queue** for efficient node selection.

**Example Thought Process:**
- Need to find shortest path to all nodes → Dijkstra's Algorithm
- Need efficient way to get next closest node → Priority Queue
- Need to store graph structure → Adjacency List (Dictionary)

## 🔑 Key Data Structure:
- Dictionary: for adjacency list representation
- Priority Queue: for Dijkstra's algorithm
- Set: to track visited nodes

---

## Plan (Pseudocode)

1. Create adjacency list representation of the graph
2. Initialize distance dictionary with infinity for all nodes
3. Set distance of source node (k) to 0
4. Use Dijkstra's algorithm to find shortest paths:
   - Use priority queue to get next closest node
   - Update distances for neighboring nodes
   - Track visited nodes

### Pseudocode Example:
```pseudo
Process:
    Create adjacency list from times
    Initialize distances = {node: infinity for all nodes}
    Set distances[k] = 0
    Initialize priority queue with (0, k)
    Initialize visited set
    
    WHILE priority queue is not empty:
        Get current distance and node from queue
        IF node in visited:
            CONTINUE
        Add node to visited
        
        FOR each neighbor, weight in adjacency list[node]:
            new_distance = current_distance + weight
            IF new_distance < distances[neighbor]:
                Update distances[neighbor] = new_distance
                Add (new_distance, neighbor) to queue
    
    IF any distance is infinity:
        RETURN -1
    RETURN maximum distance
```
## Implement

See solution.py

---

## Review
- Carefully review your implementation by checking:
  - Correctness of graph representation
  - Proper handling of infinity distances
  - Edge cases (unreachable nodes)
  - Priority queue operations
  - Visited set management

---

## Evaluate
- Time Complexity: O(E log V), where E is the number of edges and V is the number of vertices
  - Each edge is processed once
  - Priority queue operations take O(log V) time
- Space Complexity: O(V + E)
  - O(V) for distances and visited set
  - O(E) for adjacency list
  - O(V) for priority queue

---

## Optimize
- Could use a more efficient priority queue implementation
- Could use a different shortest path algorithm (e.g., Bellman-Ford) if negative weights were allowed
- Could use a different data structure for the graph if memory was a concern
