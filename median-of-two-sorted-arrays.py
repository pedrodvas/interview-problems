class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
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
        start_2 = 0
        end_2 = len(nums2)-1
        while start_1 != end_1 and start
