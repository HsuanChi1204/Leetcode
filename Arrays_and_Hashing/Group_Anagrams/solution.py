#pseudocode

#pseudocode example:
# Process:
#     Initialize empty dictionary anagrams_map

#     FOR each string in strs:
#         Sort characters in string
#         IF sorted string exists in anagrams_map:
#             Append original string to anagrams_map[sorted_string]
#         ELSE:
#             Create new list with original string in anagrams_map[sorted_string]
    
#     RETURN all values from anagrams_map

#Solution

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}

        for string in strs:
            sorted_string = sorted(string)
            sorted_string_key = "".join(sorted_string)

            if sorted_string_key in anagrams_map:
                anagrams_map[sorted_string_key].append(string)
            else:
                anagrams_map[sorted_string_key] = [string]

        return list(anagrams_map.values())
    
#test
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))

#Optimize
#use a count array instead of sorting the string


#Solution

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}

        for string in strs:
            count_array = [0] * 26
            for char in string:
                count_array[ord(char) - ord("a")] += 1

            count_array_key = tuple(count_array)

            if count_array_key in anagrams_map:
                anagrams_map[count_array_key].append(string)
            else:
                anagrams_map[count_array_key] = [string]

        return list(anagrams_map.values())
    
#test
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))

#review

