from typing import List

class Solution:
    def longestConsecutive_brute(self, nums: List[int]) -> int:
        """
        Solution 1: Brute Force Approach
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
            
        nums.sort()
        longest_streak = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:  # Skip duplicates
                if nums[i] == nums[i-1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
        
        return max(longest_streak, current_streak)
    
    def longestConsecutive_optimized(self, nums: List[int]) -> int:
        """
        Solution 2: Hash Set Approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Only check numbers that are the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak

# Test cases
def test_solutions():
    solution = Solution()
    
    # Test case 1: Simple case
    nums1 = [100,4,200,1,3,2]
    expected1 = 4
    assert solution.longestConsecutive_brute(nums1) == expected1
    assert solution.longestConsecutive_optimized(nums1) == expected1
    
    # Test case 2: With duplicates
    nums2 = [0,3,7,2,5,8,4,6,0,1]
    expected2 = 9
    assert solution.longestConsecutive_brute(nums2) == expected2
    assert solution.longestConsecutive_optimized(nums2) == expected2
    
    # Test case 3: Empty array
    nums3 = []
    expected3 = 0
    assert solution.longestConsecutive_brute(nums3) == expected3
    assert solution.longestConsecutive_optimized(nums3) == expected3
    
    # Test case 4: Single element
    nums4 = [1]
    expected4 = 1
    assert solution.longestConsecutive_brute(nums4) == expected4
    assert solution.longestConsecutive_optimized(nums4) == expected4
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solutions()
