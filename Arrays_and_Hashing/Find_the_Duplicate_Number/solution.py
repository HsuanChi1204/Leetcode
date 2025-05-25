from typing import List

class Solution:
    def findDuplicate_floyd(self, nums: List[int]) -> int:
        """
        Solution 1: Floyd's Cycle Detection (Tortoise and Hare)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Phase 1: Find the intersection point
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
    
    def findDuplicate_binary_search(self, nums: List[int]) -> int:
        """
        Solution 2: Binary Search
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        left, right = 1, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            count = 0
            
            # Count numbers <= mid
            for num in nums:
                if num <= mid:
                    count += 1
            
            # If count > mid, duplicate is in left half
            if count > mid:
                right = mid
            else:
                left = mid + 1
        
        return left

# Test cases
def test_solutions():
    solution = Solution()
    
    # Test case 1: Basic case
    nums1 = [1,3,4,2,2]
    expected1 = 2
    assert solution.findDuplicate_floyd(nums1) == expected1
    assert solution.findDuplicate_binary_search(nums1) == expected1
    
    # Test case 2: Duplicate at start
    nums2 = [3,1,3,4,2]
    expected2 = 3
    assert solution.findDuplicate_floyd(nums2) == expected2
    assert solution.findDuplicate_binary_search(nums2) == expected2
    
    # Test case 3: Duplicate at end
    nums3 = [1,2,3,4,4]
    expected3 = 4
    assert solution.findDuplicate_floyd(nums3) == expected3
    assert solution.findDuplicate_binary_search(nums3) == expected3
    
    # Test case 4: Small array
    nums4 = [1,1]
    expected4 = 1
    assert solution.findDuplicate_floyd(nums4) == expected4
    assert solution.findDuplicate_binary_search(nums4) == expected4
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solutions() 