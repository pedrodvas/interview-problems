from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        '''
        supposedely there is a faster solution than n2 for
        creating the graph

        we can actually use a bfs search, changing each of 
        the letters of the current word into a new one and testing if
        it matches some other word in our input.
        '''
        available_word_set = set()
        for i in wordList:
            available_word_set.add(i)

        seen_words = set()
        words_queue = deque()
        words_queue.append([beginWord, 1])
        seen_words.add(beginWord)
        while words_queue:
            curr_word = words_queue.popleft()
            if curr_word[0] == endWord:
                return curr_word[1]
            to_add = check_word_neighbors(curr_word, available_word_set, seen_words)
            for i in to_add:
                words_queue.append(i)
                seen_words.add(i[0])

        return 0
def check_word_neighbors(word_step: tuple[str, int], available_words: set, seen_words: set):
    ret_list = []
    word = word_step[0]
    step = word_step[1]
    for i in range(len(word)):
        for letter in range(ord('a'), ord('z')+1):
            assembled_word = word[:i]+chr(letter)+word[i+1:]
            if (assembled_word in available_words
            and assembled_word not in seen_words):
                ret_list.append([assembled_word, step+1])

    return ret_list

if __name__ == "__main__":
    sol = Solution()
    a = sol.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
    print(a)