# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers1(self, l1, l2):
        '''
        ganha de 55% em tempo e 14% em memoria
        '''
        sum = 0
        power_10 = 0
        sum += l1.val * 10**power_10
        while l1.next:
            l1 = l1.next
            power_10 += 1
            sum += l1.val * 10**power_10

        power_10 = 0
        sum += l2.val * 10**power_10
        while l2.next:
            l2 = l2.next
            power_10 += 1
            sum += l2.val * 10**power_10
            
        return_list_first = ListNode(0)
        return_list_iterating = return_list_first
        while sum != 0:
            curr_digit = sum % 10
            sum = sum // 10
            return_list_iterating.val = curr_digit
            if sum != 0:
                return_list_iterating.next = ListNode(0)
                return_list_iterating = return_list_iterating.next

        return return_list_first

    def addTwoNumbers(self, l1, l2):
        '''
        ganha de 55% em tempo e 14% em memoria
        '''
        l1_sum = 0
        power_10 = 0
        l1_sum += l1.val * 10**power_10
        while l1.next:
            l1 = l1.next
            power_10 += 1
            l1_sum += l1.val * 10**power_10

        l2_sum = 0
        power_10 = 0
        l2_sum += l2.val * 10**power_10
        while l2.next:
            l2 = l2.next
            power_10 += 1
            l2_sum += l2.val * 10**power_10
                
        total_sum = l1_sum + l2_sum
        return_list_first = ListNode(0)
        return_list_iterating = return_list_first
        while total_sum != 0:
            curr_digit = total_sum % 10
            total_sum = total_sum // 10
            return_list_iterating.val = curr_digit
            if total_sum != 0:
                return_list_iterating.next = ListNode(0)
                return_list_iterating = return_list_iterating.next
        
        return return_list_first
    
