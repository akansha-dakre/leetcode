class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        t=[]
        for i in range(0,len(nums1)):
            if nums1[i] in nums2:
                t.append(nums1[i])
                nums2.pop(nums2.index(nums1[i]))
        
        return t
                
                
        