class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

class Max_heap3(object):
    def __init__(self, val_A, list_A, val_B, list_B, val_C, list_C):
        if val_A > val_B and val_A > val_C:
            self.top = HeapNode(val_A, list_A)
            self.left = HeapNode(val_B, list_B)
            self.right = HeapNode(val_C, list_C)

        elif val_B > val_A and val_B > val_C:
            self.top = HeapNode(val_B, list_B)
            self.left = HeapNode(val_A, list_A)
            self.right = HeapNode(val_C, list_C)

        else:
            self.right = HeapNode(val_C, list_C)
            self.top = HeapNode(val_A, list_A)
            self.left = HeapNode(val_B, list_B)

    def print(self):
        print(f"top: {self.top.value} \nleft: {self.left.value} right: {self.right.value}")


class HeapNode(object):
    def __init__(self, value, list):
        self.value = value
        self.list = list


if __name__ == "__main__":
    test_heap = Max_heap3(1, [], 2, [], 3, [])
    test_heap.print()