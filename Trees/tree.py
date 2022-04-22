class tree_node:
    def __init__(self, val, right = None, left = None):
        self.val = val
        self.right_branch = None
        self.left_branch = None

def tree_search(search_val, tree_node):
    if search_val == tree_node.val or tree_node is None:
        return tree_node
    elif search_val < tree_node.val:
        return tree_search(search_val, tree_node.left_branch)
    else:
        return tree_search(search_val, tree_node.right_branch)

def tree_insert(tree_node, insert_val):
    if insert_val < tree_node.val:
        if  tree_node.left_branch is None:
            tree_node.left_branch = tree_node(insert_val)
        else:
            tree_insert(tree_node.left_branch, insert_val)
    elif insert_val > tree_node.val:
        if  tree_node.right_branch is None:
            tree_node.right_branch = tree_node(insert_val)
        else:
            tree_insert(tree_node.right_branch, insert_val)
