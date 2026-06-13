class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #the zigzag repats itself every numRows+numRows-2
        #I will create a matrix to store that
        size_pattern = numRows+numRows-2
        #will be used when the line has not straight
        #lines in it
        final_string = []
        for i in range(numRows):
            even_occurence = i
            odd_occurence = size_pattern-i
            while even_occurence < len(s) and odd_occurence < len(s):
                final_string.append(s[even_occurence])
                if odd_occurence != even_occurence:
                    final_string.append(s[odd_occurence])
                    print("hi")
                even_occurence += size_pattern
                odd_occurence += size_pattern
                print(final_string)
        
        print(final_string)
        
            

if __name__ == "__main__":
    sol = Solution()
    sol.convert("PAYPALISHIRING", 4)