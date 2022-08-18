from re import S


def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    return [[s[i], t[i]] for i in range(len(s))]

def divisors(n):
    """Returns all the divisors of N.

    >>> divisors(12)
    [1, 2, 3, 4, 6]
    """
    return [1] + [x for x in range(2, n) if n % x == 0]

def front(s, f):
    """Return S but with elements chosen by F at the front.

    >>> front(range(10), lambda x: x % 2 == 1)  # odds in front
    [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    """
    return [x for x in s if f(x)] + [x for x in s if not f(x)]

def sum_up_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_up_to_n(n-1) 
    
def reverse(s):
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    if n == 2 or n == 1:
        return n
    else:
        first_step1 = count_stair_ways(n - 1)
        first_step2 = count_stair_ways(n - 2)
        return first_step1 + first_step2

def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif k == 0:
        return 0
    else:
        return count_k(n - k, k) + count_k(n, k - 1)

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i]*i for i in range(len(s)) if i%2 == 0]