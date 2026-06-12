# this could be done with two pointers but i would be trivial.
# doing it this way makes it scalable for n arrays, although 
# this part won't be implemented.

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        index1 = 0
        index2 = 0
        middle = len(nums1)/2 + len(nums2)/2
        max_heap = Min_heap(nums1[0], nums1, nums2[0], nums2)
        while index1 + 1 + index2 + 1 < middle:
            index1, index2 = max_heap.update_list(index1, nums1, index2, nums2)

        
        return max_heap.top




class Min_heap(object):
    def __init__(self, index_A, list_A, index_B, list_B):
        if list_A[index_A] > list_B[index_B]:
            self.top = HeapNode(list_A[index_A], list_A)
            self.bottom = HeapNode(list_B[index_B], list_B)
            
        else:
            self.top = HeapNode(list_B[index_B], list_B)
            self.bottom = HeapNode(list_A[index_A], list_A)
            
    def print(self):
        print(f"top: {self.top.value} \nbottom: {self.bottom.value}")

    def update_list(self, index_A, list_A, index_B, list_B):
        if self.top.list == list_A:
            new_value = list_A[index_A+1]
        else:
            new_value = list_B[index_B+1]

        if new_value > self.bottom.value:
            self.top = HeapNode(new_value, self.top.list)
        

class HeapNode(object):
    def __init__(self, value, list):
        self.value = value
        self.list = list


if __name__ == "__main__":
    test_heap = Min_heap(1, [], 2, [], 3, [])
    test_heap.print()