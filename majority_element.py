from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #method 2
        frequency_dict = {}
        for element in nums:
            frequency_dict[element] = frequency_dict.get(element, 0) + 1
            most_frequent = max(frequency_dict, key=frequency_dict.get)
        return most_frequent
    
obj = Solution()
print(obj.majorityElement([2,3,4,2,4,4,4,5,6]))