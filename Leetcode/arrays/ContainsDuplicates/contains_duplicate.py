class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d=collections.Counter(nums)
        
        for i in range(0,len(nums)-1):
            if d[nums[i]]>1:
                return True