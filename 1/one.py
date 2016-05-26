def is_unique(s):
    """
    Check if every character is unique in string s

    Check if the character is in substring from the character to end

    O(n^2) efficiency but O(1) space
    """
    for i in xrange(len(s)):
        if s[i] in s[:i]:
            return False
    return True


def is_unique2(s):
    """
    Use a list and the int of the character will tell if that character has
    already appeared once
    """
    d = []
    for t in s:
        if d[int(t)]:
            return False
        d[int(t)] = True
    return True
