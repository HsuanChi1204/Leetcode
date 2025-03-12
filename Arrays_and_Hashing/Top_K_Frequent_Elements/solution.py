#Solution (using a heap)

from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for num in nums:
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1
        
        min_heap = []
        for num, count in nums_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (count, num))
            elif count > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (count, num))
        
        return [num for count, num in min_heap]
    
#test
print(Solution().topKFrequent([1,1,1,2,2,3], 2))
print(Solution().topKFrequent([1], 1))

#Solution (using a bucket sort)

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for num in nums:
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in nums_map.items():
            bucket[count].append(num)
        
        result = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
                    
#test
print(Solution().topKFrequent([1,1,1,2,2,3], 2))
print(Solution().topKFrequent([1], 1))
