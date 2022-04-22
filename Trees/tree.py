class tree_node:
    def __init__(self, val, right = None, left = None):
        self.val = val
        self.right_branch = None
        self.left_branch = None

def tree_search(search_val, tree_node):
    if search_val == tree_node.val or tree_node is None:
        return tree_node
    elif search_val < tree_node.val:
        tree_search(search_val, tree_node.left_branch)
    else:
        tree_search(search_val, tree_node.right_branch)