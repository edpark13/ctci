def check_permutation(s, t):
    if len(s) is not len(t):
        return False
    for r in s:
        if r not in t:
            return False
    return True
