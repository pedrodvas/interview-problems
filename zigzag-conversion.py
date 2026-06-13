class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        #the zigzag repats itself every numRows+numRows-2
        #I will create a matrix to store that
        size_pattern = numRows+numRows-2
        #will be used when the line has not straight
        #lines in it
        chars_list = []
        for i in range(numRows):
            even_occurence = i
            odd_occurence = size_pattern-i
            skip_odd = True if i==0 else False
            while even_occurence < len(s) or odd_occurence < len(s):
                if even_occurence < len(s):
                    chars_list.append(s[even_occurence])
                if not skip_odd and odd_occurence != even_occurence and odd_occurence < len(s):
                    chars_list.append(s[odd_occurence])

                even_occurence += size_pattern
                odd_occurence += size_pattern
        
        final_string = "".join(chars_list)
        return final_string
        
            

if __name__ == "__main__":
    sol = Solution()
    sol.convert("PAYPALISHIRING", 3)
    sol.convert("PAYPALISHIRING", 4)