## Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty: Medium
Topic: Array, Hash Table, Union Find
Content: 
- Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
- You must write an algorithm that runs in O(n) time.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - *What is the input format?* Unsorted array of integers
  - *Can the array contain duplicates?* Yes
  - *Can the array be empty?* Yes
  - *What if there are multiple sequences of same length?* Return any of them
  - *Is there any requirement on time/space complexity?* O(n) time
  - *Can I sort the array?* Not recommended for O(n) solution

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: nums = [100,4,200,1,3,2]
  Output: 4
  Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]
  ```

- **Edge Case:**
  ```python
  Input: nums = [0,3,7,2,5,8,4,6,0,1]
  Output: 9
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Need efficient lookup
- Is a **Dictionary** helpful? Yes, for O(1) lookups
- Consider **Hash Set** for unique elements
- Consider **Union Find** for connected components

**Example Thought Process:**
- Need to find consecutive numbers → Use hash set for O(1) lookups
- Need to avoid duplicates → Use set
- Need O(n) time → Avoid sorting
- Need to find sequences → Check neighbors

## 🔑 Key Data Structure:
- Set: for storing unique numbers and O(1) lookups
- Variables: for tracking current and longest sequence lengths

---

## Plan (Pseudocode)

### Solution 1: Brute Force
```pseudo
Process:
    Sort the array
    Initialize current and longest sequence lengths
    FOR each number in array:
        IF current number is consecutive to previous:
            Increment current sequence length
        ELSE:
            Update longest sequence length
            Reset current sequence length
    RETURN longest sequence length
```

### Solution 2: Hash Set
```pseudo
Process:
    Convert array to set
    FOR each number in set:
        IF number-1 not in set (start of sequence):
            Initialize current sequence length
            WHILE next number exists in set:
                Increment current sequence length
            Update longest sequence length
    RETURN longest sequence length
```

---

## Review
- Carefully review your implementation by checking:
  - Correctness of sequence detection
  - Proper handling of duplicates
  - Proper handling of empty array
  - Time and space complexity requirements

---

## Evaluate
### Solution 1: Brute Force
- Time Complexity: O(n log n)
  - Sorting takes O(n log n)
  - Single pass takes O(n)
- Space Complexity: O(1)
  - Only variables for tracking lengths

### Solution 2: Hash Set
- Time Complexity: O(n)
  - Single pass through array
  - O(1) lookups in set
- Space Complexity: O(n)
  - Set to store numbers

---

## Optimize
- Could use Union Find for better performance
- Could optimize memory usage
- Could handle edge cases more efficiently

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?
