class Solution:
    def decodeString(self, s: str) -> str:
        '''
        idea1: use a recursive decode string.
        each call of the function only resolves one
        string multiplication at a time.
        
        if this f only returns str, then it can't be used
        to move the iterator from calls from below
        '''
        answer, index = decode_len_string(s)
        return answer

def decode_len_string(s: str):
    return_string = ""
    i = 0
    numbers_string = ""
    while i < len(s):
        # anda pela string
        # adicionando carac ao retorno
        # normalmente
        # ao encontrar número
        # faz algo como:
        # deslocamento, parte_string = decode_len_string(s interna)

        if s[i] == '[':
            multiplier = int(numbers_string)
            numbers_string = ""

            internal_string, delta = decode_len_string(s[i+1:])
            i += delta

            return_string += multiplier*internal_string
            # stop counting the numbers
            # reset the multiplier
        elif ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
            numbers_string += s[i]
        elif s[i] == ']':
            return return_string, i+1
        else: #it is a leter
            return_string +=s[i]
        i += 1

    return return_string, i
if __name__ == "__main__":
    print(int("3")-1)
    print(decode_len_string("oi"))
    print(decode_len_string("oi2[ab3[c]]"))
    