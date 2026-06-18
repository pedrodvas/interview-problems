class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        I will expand from the center from each of the
        caracters.
        '''
        global_biggest = 0
        starting_index = 0
        for letter_index in range(len(s)):
            print("checking letter" + s[letter_index])
            biggest_even = palidrome_size_at_letter(s, letter_index, letter_index+1)
            biggest_odd = palidrome_size_at_letter(s, letter_index, letter_index)
            local_biggest = biggest_even if biggest_even > biggest_odd else biggest_odd
            if local_biggest > global_biggest:
                global_biggest = local_biggest
                starting_index = letter_index - (global_biggest - 1)//2
        #after finishing the loop the string will be copied
        #this could be done at the end and would make the 
        #solution a little bit more optmized

        return s[starting_index:starting_index+global_biggest]
        
def palidrome_size_at_letter(string, start, end):
    while start != -1 and end != len(string):
        if string[start] == string[end]:
            start -=1
            end +=1
        else:
            break
    return end-start-1

if __name__ == "__main__":
    sol = Solution()
    sol.longestPalindrome("babad")