'''Expression Tree'''

# First index = symbol, Second index = index of left node, Third index = index of right node
# -1 is used to indicate there is no child node on that branch
expr_tree = [
    ("*", 1, 2),
    ("+", 3, 4),
    ("+", 5, 6),
    ("3", -1, -1),
    ("4", -1, -1),
    ("1", -1, -1),
    ("2", -1, -1)
]

'''Tree Traversal'''

root = 0

# Recursive Tree Traversal
def post_order_traverse(curr):

    left, right = expr_tree[curr][1], expr_tree[curr][2]

    if left != -1:
        post_order_traverse(left) # traverse left subtree
    
    if right != -1:
        post_order_traverse(right) # traverse right subtree
    
    print(expr_tree[curr][0]) # traverse current node

post_order_traverse(root)