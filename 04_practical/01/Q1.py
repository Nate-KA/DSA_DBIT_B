def rotate_list(n, k):
    """
    Rotates a list by k positions
    k > 0: rotate right
    k < 0: rotate left
    """
    if not n:
        return n
    k = k % len(n) 
    return n[-k:] + n[:-k]

def reverse_list(n):
    """
    Returns a reversed version of the list
    """
    return n[-1]

 