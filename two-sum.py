class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for index,value in enumerate(nums):
            if((target-value) in my_map):
                return [my_map[target-value],index]
            my_map[value] = index
