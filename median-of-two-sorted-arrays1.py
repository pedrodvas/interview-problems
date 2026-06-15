class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median = len(nums1)/2 + len(nums2)/2 + 0.5
        i1 = 0
        i2 = 0
        while i1+i2 < median:
            if i1 >= len(nums1):
                i2 += 1
            elif i2 >= len(nums2):
                i1 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
            print(i1, i2)
        
        if i1+i2+1 > median:
            return nums1[i1]/2+nums2[i2]/2
        else:
            if nums1[i1]>nums2[i2]:
                return nums1[i1]
            else:
                return nums2[i2]