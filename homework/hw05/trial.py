"""
This class represents a player in a video game.
It tracks their name and health.
"""
class Player:
    """
    >>> player = Player("Mario")
    >>> player.name
    'Mario'
    >>> player.health
    100
    >>> player.damage(10)
    >>> player.health
    90
    >>> player.boost(5)
    >>> player.health
    95
    """
    def __init__(self, name):
        self.name = name
        self.health = 100
    
    def damage(self, amount):
        self.health -= amount

    def boost(self, amount):
        self.health += amount


"""
Clothing is a class that represents pieces of clothing in a closet. It tracks the color, category, and clean/dirty state.
"""
class Clothing:
    """
    >>> blue_shirt = Clothing("shirt", "blue")
    >>> blue_shirt.category
    'shirt'
    >>> blue_shirt.color
    'blue'
    >>> blue_shirt.is_clean
    True
    >>> blue_shirt.wear()
    >>> blue_shirt.is_clean
    False
    >>> blue_shirt.clean()
    >>> blue_shirt.is_clean
    True
    """
    def __init__(self, category, color):
        self.category = category
        self.color = color
        self.is_clean = True

    def wear(self):
        self.is_clean = False

    def clean(self):
        self.is_clean = True


"""
This class represents grades for students in a class.
"""
class StudentGrade:
    """
    >>> grade1 = StudentGrade("Arfur Artery", 300)
    >>> grade1.is_failing()
    False
    >>> grade2 = StudentGrade("MoMo OhNo", 158)
    >>> grade2.is_failing()
    True
    >>> grade1.failing_grade
    159
    >>> grade2.failing_grade
    159
    >>> StudentGrade.failing_grade
    159
    >>>
    """
    failing_grade = 159
    def __init__(self, student_name, num_points):
        self.student_name = student_name
        self.num_points = num_points

    def is_failing(self):
        return self.num_points < self.failing_grade


def path_yielder(t, value):
    """Yields all possible paths from the root of t to a node with the label
    value as a list.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(path_yielder(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = path_yielder(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = tree(0, [tree(2, [t1])])
    >>> print_tree(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = path_yielder(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    if label(t) == value:
        yield [label(t)]
    else:
        for b in branches(t):
            for a in path_yielder(b, value):
                yield [label(t)] + a


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


tree = lambda label, branches=[]: Tree(label, branches)
label = lambda t: t.label
branches = lambda t: t.branches
print_tree = lambda t: print(t)
