class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        checks the biggest substring without
        repeating characters and returns its len
        """
        biggest = 0
        beginning = 0
        current_set = set()
        for i in range(len(s)):
            if s[i] in current_set:
                while s[i] in current_set:
                    current_set.remove(s[beginning])
                    beginning += 1

            current_set.add(s[i])
            if i - beginning + 1 > biggest:
                biggest = i - beginning + 1
        
        return biggest
    
    def lengthOfLongestSubstring0(self, s):
        """
        solução errada pois não avança 
        corretamente quando encontra caractere 
        repetido
        """
        biggest = 0
        beginning = 0
        current_set = set()
        for i in range(len(s)):
            if s[i] in current_set:
                beginning = i
                current_set = set()
                current_set.add(s[i])
                continue
            

            current_set.add(s[i])
            if i - beginning + 1 > biggest:
                biggest = i - beginning + 1
        
        return biggest