class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        this code is supposed to check how many edits
        are enough to transform one word into another.
        the edits can be either:
        -deletion
        -insertion
        -replacement

        you have seen this problem before in one of your
        computer science classes, but you could not remeber
        how to solve it.

        The solution is using a dynamic programming table,
        where
        i = letters covered in the first word
        j = letters covered in the second word
        X h o r s e
        r 1 2 2 3 4
        o 2 1 2 3 4
        s 3 2 2 2 3
        e 4 3 3 3 3

        your table is probably wrong, but is on the right path.
        but why does this work?
        For empty to one char is trivial
        empty -> a -> 1 change
        a -> empty -> 1 change
        a -> b -> 1 change also
        
        checking word1[i] vs word2[j]
        chars either
        equal:
        in this case we now need to match
        word1[i-1] to word2[j-1]

        different:
        X E o i
        E 0 1 2
        o 1 0 Y
        
        Y 3 different ways:
        o->E->o->oi (above)
        o->i->oi (diagonal)
        o->oi (left)
        '''

        dp_table = [[None] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        dp_table[0][0] = 0 #empty equals empty

        for i in range(len(word1)+1):
            for j in range((len(word2)+1)):
                if i==0 or j==0:
                    dp_table[i][j] = max(len(word1[0:i]), len(word2[0:j]))
                elif word1[i-1] == word2[j-1] and i>0 and j>0:
                    dp_table[i][j] = dp_table[i-1][j-1]
                else:
                    to_check = []
                    if i > 0:
                        to_check.append(dp_table[i-1][j]+1)
                    if j > 0:
                        to_check.append(dp_table[i][j-1]+1)
                    if i>0 and j>0:
                        to_check.append(dp_table[i-1][j-1]+1)

                    dp_table[i][j] = min(to_check)

        return dp_table[len(word1)][len(word2)]


if __name__ == "__main__":
    sol = Solution()
    a = sol.minDistance(word1 = "horse", word2 = "ros")
    print(a)
    a = sol.minDistance(word1 = "a", word2 = "")
    print(a)