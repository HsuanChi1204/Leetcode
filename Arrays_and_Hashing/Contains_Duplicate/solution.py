#pseudocode

#Create a dictionary to store the numbers and their indices
#Iterate through the list of numbers
#Check if the number is already in the dictionary
#If it is, return True
#If it is not, add the number to the dictionary
#If no duplicates are found, return False

#Solution

from typing import List

class Solution:
    def containsDuplicate_set(self, nums: List[int]) -> bool:
        """
        Solution 1: Hash Set Approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    def containsDuplicate_sort(self, nums: List[int]) -> bool:
        """
        Solution 2: Sorting Approach
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

# Test cases
def test_solutions():
    solution = Solution()
    
    # Test case 1: Contains duplicate
    nums1 = [1,2,3,1]
    expected1 = True
    assert solution.containsDuplicate_set(nums1) == expected1
    assert solution.containsDuplicate_sort(nums1) == expected1
    
    # Test case 2: No duplicates
    nums2 = [1,2,3,4]
    expected2 = False
    assert solution.containsDuplicate_set(nums2) == expected2
    assert solution.containsDuplicate_sort(nums2) == expected2
    
    # Test case 3: Empty array
    nums3 = []
    expected3 = False
    assert solution.containsDuplicate_set(nums3) == expected3
    assert solution.containsDuplicate_sort(nums3) == expected3
    
    # Test case 4: Single element
    nums4 = [1]
    expected4 = False
    assert solution.containsDuplicate_set(nums4) == expected4
    assert solution.containsDuplicate_sort(nums4) == expected4
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solutions()

#Review
#Time Complexity: O(n), because I iterate the nums list once
#Space Complexity: O(n), because I use a dictionary to store the number I checked and its Index

