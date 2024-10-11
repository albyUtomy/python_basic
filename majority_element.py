class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # method 1
        # count = 0
        # candidate = None

        # # Step 1: Find candidate for majority element
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     count += 1 if num == candidate else -1

        # # Step 2: Return the candidate as the majority element
        # return candidate


        #method 2
        frequency_dict = {}
        for element in nums:
            frequency_dict[element] = frequency_dict.get(element, 0) + 1
        most_frequent = max(frequency_dict, key=frequency_dict.get)
        return most_frequent