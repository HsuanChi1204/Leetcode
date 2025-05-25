## Find the Duplicate Number
Link: https://leetcode.com/problems/find-the-duplicate-number/
Difficulty: Medium
Topic: Array, Two Pointers, Binary Search
Content: 
- Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
- There is only one repeated number in nums, return this repeated number.
- You must solve the problem without modifying the array nums and use only constant extra space.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - *What is the input format?* Array of n+1 integers in range [1,n]
  - *Can the array be empty?* No
  - *How many duplicates are there?* Exactly one number appears twice
  - *What are the constraints?* Cannot modify array, constant extra space
  - *What is the time/space complexity requirement?* Not specified, but should be efficient

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: nums = [1,3,4,2,2]
  Output: 2
  ```

- **Edge Case:**
  ```python
  Input: nums = [3,1,3,4,2]
  Output: 3
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Need to track visited numbers
- Is a **Hash Set** helpful? Yes, but violates space constraint
- Consider **Two Pointers** for cycle detection
- Consider **Binary Search** for range search

**Example Thought Process:**
- Need to find duplicate → Use cycle detection
- Need constant space → Use Two Pointers
- Need to handle range [1,n] → Use Binary Search
- Need to avoid modifying array → Use value as index

## 🔑 Key Data Structure:
- Two Pointers: for cycle detection
- Binary Search: for range search
- Value as Index: for array traversal

---

## Plan (Pseudocode)

### Solution 1: Floyd's Cycle Detection
```pseudo
Process:
    Initialize slow and fast pointers
    DO:
        Move slow pointer one step
        Move fast pointer two steps
    WHILE slow != fast
    
    Reset slow pointer
    DO:
        Move both pointers one step
    WHILE slow != fast
    
    RETURN slow
```

### Solution 2: Binary Search
```pseudo
Process:
    Initialize left and right pointers
    WHILE left < right:
        Calculate mid
        Count numbers <= mid
        IF count > mid:
            Search left half
        ELSE:
            Search right half
    RETURN left
```

---

## Review
- Carefully review your implementation by checking:
  - Correctness of cycle detection
  - Proper handling of range constraints
  - Proper handling of edge cases
  - Time and space complexity requirements

---

## Evaluate
### Solution 1: Floyd's Cycle Detection
- Time Complexity: O(n)
  - Linear time to detect cycle
- Space Complexity: O(1)
  - Only two pointers

### Solution 2: Binary Search
- Time Complexity: O(n log n)
  - Binary search: O(log n)
  - Count numbers: O(n)
- Space Complexity: O(1)
  - Only variables for pointers

---

## Optimize
- Could use value as index for faster cycle detection
- Could optimize binary search implementation
- Could handle edge cases more efficiently

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve? 