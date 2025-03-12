#group anagrams
Link: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Topic: Arrays, Hashing
Content: 
- Given an array of strings strs, group the anagrams together. You can return the answer in any order.

## 📖 Understand 

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
    - *Can the strings be empty?* No
    - *Can the strings be of different lengths?* Yes
    - *Can the strings contain special characters?* No
    - *Can I use Python to solve the problem or are there any languages you prefer me to use?* Python is preferred
    - *Do you want me to write pseudocode first or just code the result out?* I'll write pseudocode first

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: strs = ["eat","tea","tan","ate","nat","bat"]
  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
  ```

- **Edge Case:**
  ```python
  Input: strs = [""]
  Output: [[""]]
  ```

---

## Match
Identify suitable **Data Structures** or **Algorithms** if you're stuck.

- Can I solve this with a **List**? Usually sequential and O(n) for lookups.
- Is a **Set** helpful? Fast lookups, but unordered.
- Consider a **Hashtable (Dictionary)** for O(1) lookups.

---

## Plan (Pseudocode)
 data structure:
 - Hashtable (dictionary)

 algorithm:
 - Iterate through the array of strings
 - For each string, sort the string
 - Check if the sorted string is in the dictionary
 - If it is, add the string to the list of strings in the dictionary
 - If it is not, add the sorted string to the dictionary and create a new list with the string
 - Return the values of the dictionary

---

## Implement

see solution.py

---

## Review

by sorting the string:
- Time Complexity: O(n * m log m)
- Space Complexity: O(n)

by using a count array:
- Time Complexity: O(n * m)
- Space Complexity: O(n)


---

## Optimize

- I can optimize the time complexity by using a count array instead of sorting the string
- I can also optimize the space complexity by using a count array instead of a dictionary
