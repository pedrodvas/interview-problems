class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        characters_list = {}
        for i in s:
            if i in characters_list:
                characters_list[i] += 1
            else:
                characters_list[i] = 1
        print(characters_list)

        
        for i in t:
            if i in characters_list:
                characters_list[i] -= 1
        print(characters_list)

        to_change = 0
        for i in characters_list:
            if characters_list[i] > 0:
                to_change += characters_list[i]

        return abs(to_change)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSteps("aabc", "abcd"))
    print(sol.minSteps("abaaa", "babbx"))