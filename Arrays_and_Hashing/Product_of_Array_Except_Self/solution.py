from typing import List

class Solution:
    def productExceptSelf_brute(self, nums: List[int]) -> List[int]:
        """
        Solution 1: Brute Force Approach
        Time Complexity: O(n²)
        Space Complexity: O(1) excluding output array
        """
        n = len(nums)
        result = [1] * n
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    result[i] *= nums[j]
        
        return result
    
    def productExceptSelf_optimized(self, nums: List[int]) -> List[int]:
        """
        Solution 2: Prefix and Suffix Products
        Time Complexity: O(n)
        Space Complexity: O(1) excluding output array
        """
        n = len(nums)
        result = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # Calculate suffix products and combine with prefix
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result

# Test cases
def test_solutions():
    solution = Solution()
    
    # Test case 1: Simple case
    nums1 = [1,2,3,4]
    expected1 = [24,12,8,6]
    assert solution.productExceptSelf_brute(nums1) == expected1
    assert solution.productExceptSelf_optimized(nums1) == expected1
    
    # Test case 2: With zeros
    nums2 = [-1,1,0,-3,3]
    expected2 = [0,0,9,0,0]
    assert solution.productExceptSelf_brute(nums2) == expected2
    assert solution.productExceptSelf_optimized(nums2) == expected2
    
    # Test case 3: Single element
    nums3 = [1]
    expected3 = [1]
    assert solution.productExceptSelf_brute(nums3) == expected3
    assert solution.productExceptSelf_optimized(nums3) == expected3
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solutions()
