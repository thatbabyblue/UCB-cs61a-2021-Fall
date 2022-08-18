def is_n1_digit_smaller(n1, n2):
    return n1%10 <= n2%10

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        if is_n1_digit_smaller(n1, n2):
            return 10*merge(n1//10, n2) + n1%10
        else:
            return 10*merge(n1, n2//10) + n2%10

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)
    
grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)