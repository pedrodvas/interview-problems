class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ret_list = []
        for i in nums:
            ret_list.append(i)
        for i in nums:
            ret_list.append(i)
        return  ret_list