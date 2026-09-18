class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #make nums1 bigger
        #fill complete nums1 backwards
        p1 = m - 1
        p2 = n - 1
        k = p1 + p2 + 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[k] = nums1[p1]
                p1 -= 1
            else:
                nums1[k] = nums2[p2]
                p2 -= 1
            k -= 1
        while p1 >= 0:
            nums1[k] = nums1[p1]
            p1 -= 1
            k -= 1
        while p2 >= 0:
            nums1[p1 + p2 + 1] = nums2[p2]
            p2 -= 1
            k -= 1
if __name__ == "__main__":
    sol = Solution()
    sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)