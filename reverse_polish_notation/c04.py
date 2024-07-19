'''Expression Tree'''

# Fill in -1 if there are no children nodes on that branch
expr_tree = [
    ("*", _, 2),
    ("-", 3, 4),
    ("-", 5, _),
    ("+", 7, 8),
    ("/", 9, 10),
    ("5", __, -1),
    ("4", -1, -1),
    ("7", -1, -__),
    ("*", 11, 12),
    ("+", __, __),
    ("+", __, 16),
    ("18", -1, -1),
    ("3", __, -1),
    ("5", -1, -1),
    ("__", -1, -1),
    ("1", -1, __),
    ("2", -1, -1)
]

'''Tree Traversal'''

root = 0

def post_order_traverse(curr):

    left, right = expr_tree[____][1], expr_tree[____][2]

    if left != ____:
        post_order_traverse(left)
    
    if right != -1:
        post_order_traverse(____)
    
    print(expr_tree[curr][____])

post_order_traverse(____)