import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums, low, high):
            if low < high:
                pivot = findPivot(nums, low, high)
                quickSort(nums, low, pivot-1)
                quickSort(nums, pivot+1, high)
                  
        def findPivot(nums, low, high):
            pivotIdx = random.randint(low, high)
            nums[low], nums[pivotIdx] = nums[pivotIdx], nums[low]
            pivot = nums[low]
            i = low+1
            j = high

            while True:
                while(i <= j and nums[i] <= pivot):
                    i += 1
                while(i <= j and nums[j] > pivot):
                    j -= 1
                if i > j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            nums[low], nums[j] = nums[j], nums[low]
            return j

        quickSort(nums, 0, len(nums)-1)
        return nums
