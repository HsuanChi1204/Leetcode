## Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium
Topic: Array, Prefix Sum
Content: 
- Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
- You must write an algorithm that runs in O(n) time and without using the division operation.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
  - *What is the input format?* Array of integers
  - *Can the array contain zeros?* Yes
  - *Can the array contain negative numbers?* Yes
  - *What if there are multiple zeros?* Handle accordingly
  - *Is there any requirement on time/space complexity?* O(n) time, O(1) space (excluding output array)
  - *Can I use division?* No

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: nums = [1,2,3,4]
  Output: [24,12,8,6]
  ```

- **Edge Case:**
  ```python
  Input: nums = [-1,1,0,-3,3]
  Output: [0,0,9,0,0]
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Yes, for storing results
- Is a **Dictionary** helpful? Not necessary
- Consider **Prefix Product** approach
- Consider **Two Pointers** technique

**Example Thought Process:**
- Need to calculate product except self → Prefix and Suffix products
- Need to handle zeros → Special case handling
- Need O(n) time → Use prefix/suffix arrays
- Need O(1) space → Use output array for calculations

## 🔑 Key Data Structure:
- List: for storing results
- Variables: for tracking prefix and suffix products

---

## Plan (Pseudocode)

### Solution 1: Brute Force
```pseudo
Process:
    Initialize result array
    FOR each element in array:
        Calculate product of all other elements
        Store in result array
    RETURN result array
```

### Solution 2: Prefix and Suffix Products
```pseudo
Process:
    Initialize result array with 1s
    Calculate prefix products
    Calculate suffix products
    Multiply prefix and suffix products
    RETURN result array
```

---

## Review
- Carefully review your implementation by checking:
  - Correctness of product calculations
  - Proper handling of zeros
  - Proper handling of negative numbers
  - Time and space complexity requirements

---

## Evaluate
### Solution 1: Brute Force
- Time Complexity: O(n²)
  - Nested loops for each element
- Space Complexity: O(1)
  - Only output array

### Solution 2: Prefix and Suffix Products
- Time Complexity: O(n)
  - Single pass for prefix products
  - Single pass for suffix products
- Space Complexity: O(1)
  - Only output array

---

## Optimize
- Could use single pass approach
- Could handle zeros more efficiently
- Could optimize memory usage

---

## Evaluate (Self-assessment)
- Did I clearly understand the question and constraints?
- Was my solution efficient in terms of time and space?
- Did I consider edge cases and validate my solution adequately?
- Can my code readability or structure improve?
