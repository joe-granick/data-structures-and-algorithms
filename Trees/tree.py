class tree_node:
    def __init__(self, val, right = None, left = None):
        self.val = val
        self.right_branch = None
        self.left_branch = None

def tree_search(search_val, node):
    if search_val == node.val or node is None:
        return node
    elif search_val < node.val:
        return tree_search(search_val, node.left_branch)
    else:
        return tree_search(search_val, node.right_branch)

def tree_insert(node, insert_val):
    if insert_val < node.val:
        if  node.left_branch is None:
            node.left_branch = tree_node(insert_val)
        else:
            tree_insert(node.left_branch, insert_val)
    elif insert_val > node.val:
        if  node.right_branch is None:
            node.right_branch = tree_node(insert_val)
        else:
            tree_insert(node.right_branch, insert_val)
def delete_node(val, node):
    def successor():
        pass
    if node == node.val:
        pass
    else:
        pass