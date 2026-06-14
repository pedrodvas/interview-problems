class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not has_star(p) and len(p) != len(s):
            print("unmatchable size difference detected")
            return False
        curr_pattern = 0
        curr_string = 0
        while curr_pattern < len(p) and curr_string < len(s):
            print("matching "+s[curr_string:]+"-"+p[curr_pattern:])
            if curr_pattern+1 < len(p) and p[curr_pattern+1] == '*':
                minimum_times = count_minimum_times(p[curr_pattern:])
                times = 0
                while curr_string< len(s) and matches(s[curr_string], p[curr_pattern]):
                    curr_string += 1
                    times += 1
                if times < minimum_times:
                    return False
                else:
                    curr_pattern += minimum_times+2
                    
            elif matches(s[curr_string], p[curr_pattern]):
                print("absorbed " + s[curr_string])
                curr_pattern += 1
                curr_string += 1
            else:
                return False
        print("curr string is "+str(curr_string))
        if curr_string != len(s) or curr_pattern != len(p):
            return False

        return True

def has_star(s):
    for i in s:
        if i == '*':
            return True
    return False

def matches(string_char, pattern_char):
    if pattern_char == '.':
        return True
    elif pattern_char == string_char:
        return True
    else:
        return False

def count_minimum_times(p):
    curr_char_index = 2 #after the *
    while curr_char_index < len(p):
        if p[curr_char_index] == p[0]:
            curr_char_index += 1
        else:
            return curr_char_index -2
    return curr_char_index - 2

if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("mississippi", "mis*is*p*."))
    print(sol.isMatch("aa", "a*"))
    print(sol.isMatch("ab", ".*"))
    print(sol.isMatch("aaa", "a*a"))
    print(sol.isMatch("ab", ".*c"))
    print(sol.isMatch("aaa", "ab*a*c*a"))
    print(sol.isMatch("aa", "a*c*a"))