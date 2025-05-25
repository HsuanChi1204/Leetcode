## 3Sum
Link: https://leetcode.com/problems/3sum/
Difficulty: Medium
Topic: Array, Two Pointers, Sorting
Content: 
- Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
- Notice that the solution set must not contain duplicate triplets.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - *What is the input format?* Array of integers
  - *Can the array contain duplicates?* Yes
  - *Can the array be empty?* Yes
  - *What if there are multiple valid triplets?* Return all unique triplets
  - *What is the time/space complexity requirement?* Not specified, but should be efficient

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: nums = [-1,0,1,2,-1,-4]
  Output: [[-1,-1,2],[-1,0,1]]
  ```

- **Edge Case:**
  ```python
  Input: nums = []
  Output: []
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Need to track triplets
- Is a **Hash Set** helpful? Yes, for avoiding duplicates
- Consider **Two Pointers** for efficient search
- Consider **Sorting** for better organization

**Example Thought Process:**
- Need to find three numbers → Use three pointers
- Need to avoid duplicates → Sort array and skip duplicates
- Need to optimize search → Use two pointers after sorting
- Need to handle edge cases → Check array length

## 🔑 Key Data Structure:
- List: for storing triplets
- Two Pointers: for efficient search
- Sorting: for better organization and duplicate handling

---

## Plan (Pseudocode)

### Solution 1: Two Pointers
```pseudo
Process:
    Sort the array
    Initialize result list
    FOR each number as first element:
        IF number > 0:
            Break (no possible sum)
        IF number is same as previous:
            Skip (avoid duplicates)
        Use two pointers to find other two numbers
        WHILE left < right:
            Calculate sum
            IF sum == 0:
                Add triplet to result
                Skip duplicates
            ELIF sum < 0:
                Move left pointer
            ELSE:
                Move right pointer
    RETURN result
```

### Solution 2: Hash Set
```pseudo
Process:
    Sort the array
    Initialize result set
    FOR each number as first element:
        IF number > 0:
            Break
        IF number is same as previous:
            Skip
        Use hash set to find third number
        FOR each number as second element:
            Calculate required third number
            IF third number in set:
                Add triplet to result
    RETURN result
```

---

## Review
- Carefully review your implementation by checking:
  - Correctness of triplet finding
  - Proper handling of duplicates
  - Proper handling of edge cases
  - Time and space complexity requirements

---

## Evaluate
### Solution 1: Two Pointers
- Time Complexity: O(n²)
  - Sort: O(n log n)
  - Two pointers: O(n²)
- Space Complexity: O(1)
  - Only variables for pointers

### Solution 2: Hash Set
- Time Complexity: O(n²)
  - Sort: O(n log n)
  - Hash set operations: O(n²)
- Space Complexity: O(n)
  - Hash set for storing numbers

---

## Optimize
- Could use early termination for positive numbers
- Could optimize memory usage
- Could handle edge cases more efficiently

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve? 