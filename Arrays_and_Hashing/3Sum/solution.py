from typing import List

class Solution:
    def threeSum_two_pointers(self, nums: List[int]) -> List[List[int]]:
        """
        Solution 1: Two Pointers Approach
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        if len(nums) < 3:
            return []
            
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Early termination if first number is positive
            if nums[i] > 0:
                break
                
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for second number
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # Skip duplicates for third number
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result
    
    def threeSum_hash_set(self, nums: List[int]) -> List[List[int]]:
        """
        Solution 2: Hash Set Approach
        Time Complexity: O(n²)
        Space Complexity: O(n)
        """
        if len(nums) < 3:
            return []
            
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Early termination if first number is positive
            if nums[i] > 0:
                break
                
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])
                
                if complement in seen:
                    result.append([nums[i], complement, nums[j]])
                    # Skip duplicates for second number
                    while j + 1 < len(nums) and nums[j] == nums[j+1]:
                        j += 1
                seen.add(nums[j])
                
        return result

# Test cases
def test_solutions():
    solution = Solution()
    
    # Test case 1: Basic case
    nums1 = [-1,0,1,2,-1,-4]
    expected1 = [[-1,-1,2],[-1,0,1]]
    assert sorted(solution.threeSum_two_pointers(nums1)) == sorted(expected1)
    assert sorted(solution.threeSum_hash_set(nums1)) == sorted(expected1)
    
    # Test case 2: Empty array
    nums2 = []
    expected2 = []
    assert solution.threeSum_two_pointers(nums2) == expected2
    assert solution.threeSum_hash_set(nums2) == expected2
    
    # Test case 3: No solution
    nums3 = [1,2,3,4,5]
    expected3 = []
    assert solution.threeSum_two_pointers(nums3) == expected3
    assert solution.threeSum_hash_set(nums3) == expected3
    
    # Test case 4: All zeros
    nums4 = [0,0,0]
    expected4 = [[0,0,0]]
    assert solution.threeSum_two_pointers(nums4) == expected4
    assert solution.threeSum_hash_set(nums4) == expected4
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solutions() 