class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        dumb solution would be checking every substring of s (n²)
        contains all chars of t (n) making a n³ solution.

        What other ways can we make that operation? We can start
        by assuming s contains t. After that, we initialize one
        pointer on each side of s, and if s[pointer] not in t 
        then we can walk with said pointer.
        The problem with this approach is that if a character repeats
        on both sides, then we wouldn't let our substring minimize
        itself.
        Can this be fixed by creating a hash that its V stores the
        amount of times that each char of t has appeared?
        
        What about two pointers? We can start by initializing both
        on s[0], and we walk with pright until all chars of t are
        covered (this will be stored in a hash). If all chars are
        covered, then we will walk with the left pointer. This works
        because if somehow the minimum substring is covered by the
        two pointers, then the pleft would walk until we reach the
        minimum size. We only would need to store the minimum seen
        until current iteration
        """
        amount_letters_hash = {}
        total_letters_missing = len(t)
        for i in range(len(t)):
            if t[i] in amount_letters_hash:
                amount_letters_hash[t[i]] += 1
            else:
                amount_letters_hash[t[i]] = 1
        print(f"letter hash is {amount_letters_hash}")
        print(f"total letters is {total_letters_missing}")

        #while walking with pright, if we find a letter that is
        #in t, we decrease the counter in the hash by one
        #while this value is above 0 (so we don't count duplicates)
        #when walking with pleft, we do the opposite of the pright
        #both borders are inclusive*
        pleft, pright = 0, 0
        minimum = (-1, len(s)-1)
        total_letters_missing = put_hash(s[pright], total_letters_missing, amount_letters_hash)
        print(f"letter hash is {amount_letters_hash}")
        print(f"total letters missing is {total_letters_missing}")
        while pright < len(s):
            print(f"=======new iteration==========")
            print(f"current substring is {s[pleft:pright+1]}")
            print(f"amount of letters missing from t is {total_letters_missing}")
            if total_letters_missing > 0:
                pright += 1
                if s[pright] in amount_letters_hash:
                    total_letters_missing = put_hash(s[pright], total_letters_missing, amount_letters_hash)
            else:
                current_complete_substring = pright - pleft
                old_substring_size = minimum[1] - minimum[0]
                if current_complete_substring < old_substring_size:
                    minimum = (pleft, pright)

                print(f"checking presence of {s[pleft]}")
                if s[pleft] in amount_letters_hash:
                    total_letters_missing = remove_hash(s[pleft], total_letters_missing, amount_letters_hash)
                pleft += 1

        print(f"current minimum indexes are {minimum}")
def put_hash(letter, total_letters, letters_hash):
    letters_hash[letter] -= 1
    if letters_hash[letter] >= 0:
        total_letters -= 1
    return total_letters

def remove_hash(letter, total_letters, letters_hash):
    letters_hash[letter] += 1
    if letters_hash[letter] >= 1:
        total_letters += 1
    return total_letters

if __name__ == "__main__":
    sol = Solution()
    a = "01234"
    print(f"a cut is {a[0:2]}")
    sol.minWindow(s = "ADOBECODEBANC", t = "ABC")