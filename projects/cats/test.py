def reverse(n):
    """Returns N with the digits reversed.
    >>> reverse_digits(123)
    321
    """
    if n < 10:
        return n
    else:
        return (n%10)*(10**(L(n)-1)) + reverse(n//10)

def L(n):
    if n < 10:
        return 1
    else:
        return L(n//10) + 1
