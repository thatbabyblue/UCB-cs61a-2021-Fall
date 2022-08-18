from locale import currency


def termified(n, term):
    """Returns every the result of calling TERM
    on each element in the range from 0 to N (inclusive).

    >>> termified(5, lambda x: 2 ** x)
    [1, 2, 4, 8, 16, 32]
    """
    return list(map(term, range(n + 1)))


def divisors(n):
    """Returns all the divisors of N.

    >>> divisors(12)
    [1, 2, 3, 4, 6]
    """
    return list(filter(lambda x: n%x == 0, range(1, n)))


def matches(a, b):
    """Return the number of values k such that A[k] == B[k].
    >>> matches([1, 2, 3, 4, 5], [3, 2, 3, 0, 5])
    3
    >>> matches("abdomens", "indolence")
    4
    >>> matches("abcd", "dcba")
    0
    >>> matches("abcde", "edcba")
    1
    >>> matches("abcdefg", "edcba")
    1
    """
    return sum([1 for x, y in zip(a, b) if x == y])


def list_o_lists(n):
    """Assuming N >= 0, return the list consisting of N lists:
    [1], [1, 2], [1, 2, 3], ... [1, 2, ... N].
    >>> list_o_lists(0)
    []
    >>> list_o_lists(1)
    [[1]]
    >>> list_o_lists(5)
    [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
    """
    return [list(range(1, i + 1)) for i in range(1, n + 1)]


def palindrome(s):
    """Return whether s is the same sequence backward and forward.
    ​
    >>> palindrome([3, 1, 4, 1, 5])
    False
    >>> palindrome([3, 1, 4, 1, 3])
    True
    >>> palindrome('seveneves')
    True
    >>> palindrome('seven eves')
    False
    """
    '''return all(a == b for a, b in zip(s, reversed(s))) or'''
    return list(reversed(s)) == list(s)


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.
    Iterate through the items such that if the same iterator is passed into
    the function twice, it continues in the second call at the point it left
    off in the first.
 
    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    last_val = None
    cnt = 0
    while True:
        val = next(t)
        if last_val == None or val != last_val:
            last_val, cnt = val, 1
        else:
            cnt += 1
        if cnt == k:
            return val


def repeatedalter(t, k):
    """Return the first value in iterator T that appears K times in a row.
    Iterate through the items such that if the same iterator is passed into
    the function twice, it continues in the second call at the point it left
    off in the first.
 
    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    last_val = None
    def helper(k):
        nonlocal last_val
        nonlocal t
        cnt = 0

        while True:
            val = next(t)
            if last_val == None or val != last_val:
                last_val, cnt = val, 1
            else:
                cnt += 1
            if cnt == k:
                return val
    return helper(k)


def count_occurence(lst, entry):
    n = 0
    b = len(lst)
    for i in range(b):
        if lst[i] == entry:
            n += 1
    return n


def countdown(n):
    """
    Generate a countdown of numbers from N down to 'blast off!'.
    >>> c = countdown(3)
    >>> next(c)
    3
    >>> next(c)
    2
    >>> next(c)
    1
    >>> next(c)
    'blast off!'
    """
    while n > 0:
        yield n
        n = n - 1
    yield 'blast off!'


def generate_virfib():
    """Generate the next Virahanka-Fibonacci number.
    >>> g = generate_virfib()
    >>> next(g)
    0
    >>> next(g)
    1
    >>> next(g)
    1
    >>> next(g)
    2
    >>> next(g)
    3
    """
    prev = 0
    curr = 1
    yield 0
    yield 1
    while True:
        prev, curr = curr, prev + curr
        yield curr
