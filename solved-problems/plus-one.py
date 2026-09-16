class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        ret_list = []
        carry = 1
        for i in range(len(digits)):
            curr_index = len(digits)-i-1
            curr_digit = digits[curr_index]
            result = carry + curr_digit
            if result >= 10:
                carry = 1
                result -= 10
            else:
                carry = 0
            ret_list.append(result)
        if carry == 1:
            ret_list.append(1)
        ret_list.reverse()
        return ret_list
            
if __name__ == "__main__":
    sol = Solution()
    sol.plusOne(digits = [7,8,4])