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
        median = len(nums1)/2 + len(nums2)/2 + 0.5
        i1 = 0
        i2 = 0
        while i1+i2 < median:
            if nums1[i1] < nums2[i2] and i1 < len(nums1)-1:
                i1 += 1
            else:
                i2 += 1
            print(i1, i2)
        
        if i1+i2+1 > median:
            return i1/2+i2/2
        else:
            if nums1[i1]>nums2[i2]:
                return nums1[i1]
            else:
                return nums2[i2]
        
class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        index1 = 0
        index2 = 0
        print("indexes are:")
        print(index1, index2)
        middle = len(nums1)/2 + len(nums2)/2
        max_heap = Min_heap(index1, nums1, index2, nums2)
        while index1 + index2 + 1 < middle:
            index1, index2 = max_heap.update_heap(index1, nums1, index2, nums2)
            print("indexes are:")
            print(index1, index2)

        return max_heap.top.value




class Min_heap(object):
    def __init__(self, index_A, list_A, index_B, list_B):
        if list_A[index_A] < list_B[index_B]:
            self.top = HeapNode(list_A[index_A], list_A)
            self.bottom = HeapNode(list_B[index_B], list_B)
            
        else:
            self.top = HeapNode(list_B[index_B], list_B)
            self.bottom = HeapNode(list_A[index_A], list_A)

    def print_heap(self):
        print("top | bottom = " + str(self.top.value) + " | " + str(self.bottom.value))

    def update_heap(self, index_A, list_A, index_B, list_B):
        if self.top.list == list_A:
            new_value = list_A[index_A+1]
            new_value_list = list_A
            index_A += 1
        else:
            new_value = list_B[index_B+1]
            new_value_list = list_B
            index_B += 1
        
        if new_value < self.bottom.value:
            self.top.value = new_value
            self.top.list = new_value_list
            #self.bottom doesn't have to be updated
        else:
            self.top.value = self.bottom.value
            self.top.list = self.bottom.list
            self.bottom.value = new_value
            self.bottom.list = new_value_list
        
        return index_A, index_B

        

class HeapNode(object):
    def __init__(self, value, list):
        self.value = value
        self.list = list


if __name__ == "__main__":
    feed_list1 = [11, 21, 41 ,61]
    feed_list2 = [22, 22, 32, 32]
    test_heap = Min_heap(0, feed_list1, 0, feed_list2)
    test_heap.print_heap()
    print(0, 0)
    i1,i2 = test_heap.update_heap(0, feed_list1, 0, feed_list2)
    test_heap.print_heap()
    print(i1, i2)
    i1,i2 = test_heap.update_heap(i1, feed_list1, i2, feed_list2)
    test_heap.print_heap()
    print(i1, i2)
    i1,i2 = test_heap.update_heap(i1, feed_list1, i2, feed_list2)
    test_heap.print_heap()
    print(i1, i2)
    i1,i2 = test_heap.update_heap(i1, feed_list1, i2, feed_list2)
    test_heap.print_heap()
    print(i1, i2)

    sol = Solution()
    median = sol.findMedianSortedArrays([1,3], [2])
    print("returned " + str(median))