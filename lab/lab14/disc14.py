import re
from lab14 import Tree
def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    """
    if x == y:
        return [[x]]
    elif 2 * x > y:
        return [list(range(x, y + 1))]
    else:
        a = [[x] + path1 for path1 in paths(x + 1, y)]
        b = [[x] + path2 for path2 in paths(2 * x, y)]
        return a + b

def reverse(lst):
    """Reverses lst using mutation.

    >>> original_list = [5, -1, 29, 0]
    >>> reverse(original_list)
    >>> original_list
    [0, 29, -1, 5]
    >>> odd_list = [42, 72, -8]
    >>> reverse(odd_list)
    >>> odd_list
    [-8, 72, 42]
    """
    a = len(lst)
    for i in range(a // 2):
        x = lst[i]
        lst[i] = lst[a - i - 1]
        lst[a - i - 1] = x

def deep_map(f, link):
    """Return a Link with the same structure as link but with fn mapped over
    its elements. If an element is an instance of a linked list, recursively
    apply f inside that linked list as well.

    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(deep_map(lambda x: x * x, s))
    <1 <4 9> 16>
    >>> print(s) # unchanged
    <1 <2 3> 4>
    >>> print(deep_map(lambda x: 2 * x, Link(s, Link(Link(Link(5))))))
    <<2 <4 6> 8> <<10>>>
    """
    if link is Link.empty:
        return link
    elif isinstance(link.first, Link):
        return Link(deep_map(f, link.first), deep_map(f, link.rest))
    else:
        return Link(f(link.first), deep_map(f, link.rest))


def greetings(message):
    """
    Returns whether a string is a greeting. Greetings begin with either Hi, Hello, or
    Hey (either capitalized or lowercase), and/or end with Bye (either capitalized or lowercase) optionally followed by
    an exclamation point or period.

    >>> greetings("Hi! Let's talk about our favorite submissions to the Scheme Art Contest")
    True
    >>> greetings("Hey I just figured out that when I type the Konami Code into cs61a.org, something fun happens")
    True
    >>> greetings("I'm going to watch the sun set from the top of the Campanile! Bye!")
    True
    >>> greetings("Bye Bye Birdie is one of my favorite musicals.")
    False
    >>> greetings("High in the hills of Berkeley lived a legendary creature. His name was Oski")
    False
    >>> greetings('Hi!')
    True
    >>> greetings("bye")
    True
    """
    return bool(re.search(r'^(((Hi|hi)|(Hey|hey)|(Hello|hello))\b)|(\b(Bye|bye)[!\.]?)$', message))


def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth)
    level have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    def helper_rev(t, flag):
        if t.is_leaf():
            None
        if flag:
            for i in range(len(t.branches)//2):
                midagent = t.branches[i].label
                t.branches[i].label = t.branches[-(i+1)].label
                t.branches[-(i+1)].label = midagent
        if flag:
            flag = False
        else:
            flag = True
        for s in t.branches:
            helper_rev(s, flag)
    return helper_rev(t, True)