# Moore's Voting Algo
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0;
        element = None
         
        for i in range(len(nums)):
            if count == 0:
                element = nums[i]
                count = 1
            elif nums[i] == element:
                count += 1
            else: count -= 1
        
        return element
