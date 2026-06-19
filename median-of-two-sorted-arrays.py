import bisect

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        '''
        idea is to discard the halves of each
        list successively
        why would this work?
        given
        list1 = abcd efgh -> mid =d
        list2 = mnop q rstu -> mid =q
        if d<q and the lists are ordered
        then:
            abc are smaller than q
            rstu are bigger than d
            we can discard 3 (the smaller size of subset)
            elements from each list

            could we discard 4?
            yes, because we already found out that rstu are
            all bigger than d, so we will discard
            abcd from list 1
            rstu from list 2
        if one of the lists only has one or two elements,
        then we insert them into the other one
        '''
        start_1 = 0
        end_1 = len(nums1)-1
        mid_1 = (start_1 + end_1)//2
        start_2 = 0
        end_2 = len(nums2)-1
        mid_2 = (start_2 + end_2)//2
        while (end_1-start_1)>1 and (end_2-start_2)>1:
            mid_1 = (start_1 + end_1)//2
            mid_2 = (start_2 + end_2)//2
            delta_1 = mid_1 - start_1
            delta_2 = mid_2 - start_2
            delta = delta_1 if delta_1 < delta_2 else delta_2
            if nums1[mid_1] < nums2[mid_2]:
                # we can discard the numbers to the left of mid_1
                # and to the right of mid_2
                # in the same amount
                start_1 += delta
                end_2 -= delta
            elif nums1[mid_1] > nums2[mid_2]:
                # here we do the opposite
                # we discard N numbers to right of mid_1
                # and same N numbers to the left of mid_2
                end_1 -= delta
                start_2 += delta
            else: #equal
                # can we actually return this index?
                start_1 += delta
                end_1 -= delta
                start_2 += delta
                end_2 -= delta
         
        nums1 = nums1[start_1:end_1+1]
        nums2 = nums2[start_2:end_2+1]
        # the rest of the problem will be dealt with after this loop
        # you can maybe create a function and use it with bisect maybe
        # I just need to look for the insertion index of each element
        # for each one of them that is smaller than the median of the bigger list
        # we decrease the RETURN median by 1//2
        # so global_median = (len(bigger_list) - amount_smaller_than_local_median)//2
        # with this value, can I try to extract an element from a list using key=lambda x: etc?

        smaller = nums1 if len(nums1) < len(nums2) else nums2
        bigger = nums1 if len(nums1)>= len(nums2) else nums2
        total_length = len(bigger)+len(smaller)
        median_index = total_length//2

        if total_length % 2 == 0:
            median1 = get_elem_from_merged_bonus(bigger, smaller, median_index)
            median2 = get_elem_from_merged_bonus(bigger, smaller, median_index-1)
            return (median1+median2)/2
        median = get_elem_from_merged_bonus(bigger, smaller, median_index)
        return median

def get_elem_from_merged_bonus(nums: list[int], bonus: list[int], index: int):

    indexes_list = [bisect.bisect_left(nums, i) for i in bonus]
    # space transformation
    for i in range(len(indexes_list)):
        if index <= indexes_list[i]:
            #doesn't need to be dislocated
            if index == indexes_list[i]:
                print("here")
                return bonus[i]
            return nums[index]
        index -= 1
    
    return nums[index]
    
    
if __name__ == "__main__":
    sol = Solution()
    a = sol.findMedianSortedArrays(nums1 = [1,3,5,7,89], nums2 = [2,3,4,5])
    print(a)
    a = sol.findMedianSortedArrays([1,2],[3,4])
    print(a)
