from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        '''
        supposedely there is a faster solution than n2 for
        creating the graph

        we can actually use a bfs search, changing each of 
        the letters of the current word into a new one and testing if
        it matches some other word in our input.
        '''
        
        word_transformation_graph = defaultdict(list)
