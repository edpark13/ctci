def palindrome_permutation(s):
    s = s.lower().replace(" ", "")
    d = {}
    for t in s:
        try:
            d[t] = d[t] + 1
        except KeyError:
            d[t] = 1
    for e in d:
        if d[e] % 2 is not 0 and len(s) % 2 is 0:
            return False
    return True
