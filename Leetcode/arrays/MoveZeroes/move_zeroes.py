class Solution(object):
    
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #similar to quick sort logic
        l=0
        for r in range(0,len(nums)):
            if nums[r]:
                #swap two numbers
                nums[r],nums[l]=nums[l],nums[r] 
                l+=1

        return nums
                    
                    
        