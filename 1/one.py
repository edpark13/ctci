def is_unique(s):
    for i in xrange(len(s)):
        if s[i] in s[:i]:
            return False
    return True
