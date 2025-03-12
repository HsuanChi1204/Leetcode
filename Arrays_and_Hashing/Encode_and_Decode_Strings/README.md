# Encode and Decode Strings
link: https://leetcode.com/problems/encode-and-decode-strings/
difficulty: Medium
topic: Arrays, String, Design
content: 
- Design an algorithm to encode a list of strings to a string. The encoded string is then sent to a receiver, who can decode the string back to the original list of strings.

## 📖 Understand     

### 📌 Step-by-step Process:
- **Read the question out loud**.
- **Clarify the following details**:
    - *Can the encoded string be empty?* Yes
    - *Can the encoded string contain delimiters or special characters?* Yes
    - *Is there a specific delimiter or encoding format to use?* No, you can choose any format
    - *Can I use Python to solve the problem or are there any languages you prefer me to use?* Python is preferred  
    - *Do you want me to write pseudocode first or just code the result out?* I'll write pseudocode first

### Example Test Cases:
- **Happy Case:**
  ```python
  Input: strs = ["lint","code","love","you"]
  Output: ["lint","code","love","you"]  
  ```

- **Edge Case:**
  ```python
  Input: strs = []
  Output: []
  ```   

---

## Match    
Identify suitable **Data Structures** or **Algorithms** if you're stuck.    

- Can I solve this with a **List**? Usually sequential and O(n) for lookups.
- Is a **Set** helpful? Fast lookups, but unordered.
- Consider using **Delimiter** to separate strings
- Consider using **Length Encoding** to encode string length
- Consider using **Escape Characters** to handle special characters

---

## Plan (Pseudocode)    

Process:
    Initialize empty string result
    FOR each string in strs:
        Add string length to result
        Add string to result
    RETURN result

Process:
    Initialize empty list result
    Initialize current index i = 0
    WHILE i < length of encoded string:         
        Get string length from encoded string
        Get string from encoded string
        Add string to result
        Increment i by string length + delimiter length
    RETURN result

---

## Implement

see solution.py

---

## Review   

- Time Complexity: O(n)
- Space Complexity: O(n)



