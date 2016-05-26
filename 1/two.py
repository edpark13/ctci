def check_permutation(s, t):
    """
    Check if s and t are permutations of each other

    Check if each character in s is in t
    this solution is incorrect because there can be a situation when s and t
    are the same length but have different number of a character.
    Ex. aarp != arrp

    but efficiency is O(n^2) space is O(1)
    """
    if len(s) is not len(t):
        return False
    for r in s:
        if r not in t:
            return False
    return True


def cp_sort(s, t):
    """
    Sort s and t and check if they are equal to each other

    O(nlogn + n) O(1)
    """
    if len(s) != len(t):
        return False
    return ''.join(sorted(s)) == ''.join(sorted(t))


def cp_dict(s, t):
    """
    Use a dictionary to count number of times a character occur is s
    then use that dict and subtract number of times a char occur in t
    """
    if len(s) != len(t):
        return False
    d = {}
    for q in s:
        try:
            d[q] += 1
        except KeyError:
            d[q] = 1
    for r in t:
        try:
            d[r] -= 1
            if d[r] < 0:
                return False
        except KeyError:
            return False
    return True
