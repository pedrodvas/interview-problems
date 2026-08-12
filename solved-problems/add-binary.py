class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return_chars = []
        i = 0
        carry = 0
        while i < len(a) or i < len(b):
            pos_a = len(a)-i-1
            pos_b = len(b)-i-1
            print(f"pos_a = {pos_a}")
            print(f"pob_b = {pos_b}")
            if i < len(a):
                digit_a = ord(a[pos_a]) - ord('0')
            else:
                digit_a = 0

            if i < len(b):
                digit_b = ord(b[pos_b]) - ord('0')
            else:
                digit_b = 0
            curr_sum = carry + digit_a + digit_b

            if curr_sum == 0:
                return_chars.append("0")
                carry = 0
            elif curr_sum == 1:
                return_chars.append("1")
                carry = 0
            elif curr_sum == 2:
                return_chars.append("0")
                carry = 1
            elif curr_sum == 3:
                return_chars.append("1")
                carry = 1
            i +=1

        if carry == 1:
            return_chars.append("1")
        return_chars.reverse()
        return "".join(return_chars)

if __name__ == "__main__":
    sol = Solution()
    a = sol.addBinary(a = "11", b = "11")
    print(a)