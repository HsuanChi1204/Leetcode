#Top K Frequent Elements

Link: https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: Medium
Topic: Arrays, Hashing, Sorting
Content: 
- Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## 📖 Understand     

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
    - *Can the array be empty?* No
    - *Can the array contain negative numbers?* Yes
    - *Can the array contain duplicates?* Yes
    - *Can I use Python to solve the problem or are there any languages you prefer me to use?* Python is preferred  
    - *Do you want me to write pseudocode first or just code the result out?* I'll write pseudocode first

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: nums = [1,1,1,2,2,3], k = 2
  Output: [1,2] or [2,1]
  ```

- **Edge Case:**
  ```python
  Input: nums = [1], k = 1
  Output: [1]   
  ```

---

## Match    
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Usually sequential and O(n) for lookups.
- Is a **Set** helpful? Fast lookups, but unordered.
- Consider a **Hashtable (Dictionary)** for O(1) lookups.   
- Consider a **Heap** for efficient priority queue operations.
- Consider a **Bucket Sort** for efficient sorting of elements by frequency.
---

## Plan (Pseudocode)    

by using a heap:
Process:
    Initialize empty dictionary nums_map
    
    FOR each number in nums:
        IF number exists in nums_map:
            Increment count
        ELSE:
            Add number with count 1
            
    Initialize min heap
    FOR each number, count in nums_map:
        IF heap size < k:
            Add (count, number) to heap
        ELSE IF current count > smallest count in heap:
            Remove smallest from heap
            Add (count, number) to heap
            
    RETURN array of numbers from heap

by using a bucket sort:
Process:
    Initialize empty dictionary nums_map
    
    FOR each number in nums:
        IF number exists in nums_map:
            Increment count
        ELSE:
            Add number with count 1
            
    Initialize bucket list with empty lists
    FOR each number, count in nums_map:
        Add number to bucket[count]
        
    Initialize result list
    FOR i in range(len(bucket) - 1, -1, -1):
        FOR number in bucket[i]:
            Add number to result list
            IF len(result) == k:
                RETURN result
---

## Implement

see solution.py 

---

## Review

by using a heap:
- Time Complexity: O(n log k)
- Space Complexity: O(n)    

by using a bucket sort:
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Optimize

- Use a bucket sort to improve the time complexity  


