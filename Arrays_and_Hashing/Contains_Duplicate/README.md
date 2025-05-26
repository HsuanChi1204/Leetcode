## Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Topic: Array, Hash Table, Sorting
Content: 
- Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - *What is the input format?* Array of integers
  - *Can the array be empty?* Yes
  - *Can the array contain duplicates?* Yes
  - *What is the time/space complexity requirement?* Not specified, but should be efficient

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: nums = [1,2,3,1]
  Output: true
  ```

- **Edge Case:**
  ```python
  Input: nums = [1,2,3,4]
  Output: false
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Need to track visited numbers
- Is a **Hash Set** helpful? Yes, for O(1) lookups
- Consider **Sorting** for comparison
- Consider **Hash Map** for counting

**Example Thought Process:**
- Need to find duplicates → Use Hash Set
- Need efficient lookups → Use Hash Set
- Need to track counts → Use Hash Map
- Need to compare adjacent elements → Use Sorting

## 🔑 Key Data Structure:
- Hash Set: for O(1) lookups
- Hash Map: for counting occurrences
- Sorting: for comparing adjacent elements

---

## Plan (Pseudocode)

### Solution 1: Hash Set
```pseudo
Process:
    Initialize empty set
    FOR each number in array:
        IF number in set:
            RETURN true
        Add number to set
    RETURN false
```

### Solution 2: Sorting
```pseudo
Process:
    Sort the array
    FOR each number in array:
        IF current number equals previous number:
            RETURN true
    RETURN false
```

---

## Review
- Carefully review your implementation by checking:
  - Correctness of duplicate detection
  - Proper handling of edge cases
  - Time and space complexity requirements

---

## Evaluate
### Solution 1: Hash Set
- Time Complexity: O(n)
  - Single pass through array
  - O(1) lookups in set
- Space Complexity: O(n)
  - Set to store numbers

### Solution 2: Sorting
- Time Complexity: O(n log n)
  - Sorting takes O(n log n)
  - Single pass takes O(n)
- Space Complexity: O(1)
  - Only variables for comparison

---

## Optimize
- Could use early termination in Hash Set solution
- Could optimize memory usage in Sorting solution
- Could handle edge cases more efficiently

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve? 