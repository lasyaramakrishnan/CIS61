def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

#Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

#Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    return True

def is_leaf(tree):
    return not branches(tree)

#Test Trees
t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
t2 = tree('A', [tree('B'), tree('C', [tree('D'), tree('E')])])
t3 = tree(8,
          [tree(4,
                [tree(2), tree(3)]),
           tree(3,
                [tree(1), tree(1,
                               [tree(1), tree(1)])])])

def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and False otherwise.
    >>> scrat = tree('acorn')
    >>> acorn_finder(scrat)
    True
    >>> sproul=tree('roots',[tree('branch1',[tree('leaf'),tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """
    "*** YOUR CODE HERE ***"
    if label(t) == 'acorn':
        return True
    for branch in branches(t):
        if acorn_finder(branch):
            return True
    return False

def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label that appears 
    in vals removed.  Return None if the entire tree is pruned away.
    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,[tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        if (label(t) in vals):
            return None
    new_branches = []
    for b in branches(t):
        pruned_branch = prune_leaves(b, vals)
        if pruned_branch:
            new_branches += [pruned_branch]
    return tree(label(t), new_branches)

def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5
    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE***"
    if is_leaf(t):
      return tree(label(t), [tree(x) for x in vals])
    return tree(label(t), [sprout_leaves(b, vals) for b in branches(t)])


def height(t): 
    """Return the height of a tree. 
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)]) 
    >>> height(t) 
    2
    """
    "*** YOUR CODE HERE***"
    if is_leaf(t):
        return 0
    return_height = 0
    for b in branches(t):
        return_height = max(height(b), return_height)
    return return_height + 1

def double_tree(t): 
    """Return a tree with the square of every element in t 
    >>> numbers = tree(1,
                       [tree(2,
                             [tree(3),
                              tree(4)]),
                       tree(5,
                            [tree(6,
                                  [tree(7)]),
                             tree(8)])]) 
    >>> print_tree(double_tree(numbers)) 
    2
      4
        6
        8
      10
        12
          14
        16
    """
    "*** YOUR CODE HERE***"
    if is_empty(t):
        return tree()
    else:
        value = root(t) * 2
        children = [double_tree(child) for child in branches(t)]

def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE***"
    if t1 is None:
      return t2
    if t2 is None:
      return t1

    new_label = label(t1) + label(t2)
    t1_branches, t2_branches = branches(t1), branches(t2)
    length_t1, length_t2 = len(t1_branches), len(t2_branches)

    if length_t1 < length_t2:
        t1_branches += [None for _ in range(length_t1, length_t2)]
    elif len(t1_branches) > len(t2_branches):
        t2_branches += [None for _ in range(length_t2, length_t1)]
    return tree(new_label, [add_trees(b1, b2) for b1, b2, in zip(t1_branches, t2_branches)])


        return tree(value, children)