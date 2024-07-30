def is_palindrome(self, s: str):
    len_s = len(s)
    # abcde 5/2 = 2.5, [0,2) = (4,2]
    # abcd 4/2 = 2, [0,1]=[3,2]
    # abc 3/2 = 1.5, 0,1 = 2,1

    if len_s % 2 == 0:
        halfway_index = len_s//2
        forward = s[:halfway_index]
        backward = s[len_s:halfway_index-1:-1]
        return forward == backward
    else:
        halfway_index = len_s//2
        forward = s[:halfway_index]
        backward = s[len_s:halfway_index:-1]
        return forward == backward
