import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        letter_count_dict = {}

        for i in s:
            if i in letter_count_dict:
                letter_count_dict[i] += 1
            else:
                letter_count_dict[i] = 1


        letter_count_heap = []
        for i in letter_count_dict:
            heapq.heappush(letter_count_heap, [-letter_count_dict[i], i])
        print(letter_count_heap)
        ret_list = []
        last = [1, None]
        for i in range(len(s)):
            print(letter_count_heap)
            heapq.heappush(letter_count_heap, last)
            to_use = heapq.heappop(letter_count_heap)
            to_use[0] += 1
            ret_list.append(to_use[1])
            last = to_use

        print(ret_list)
        return "".join(ret_list)
    
if __name__ == "__main__":
    sol = Solution()
    sol.reorganizeString("sfffp")