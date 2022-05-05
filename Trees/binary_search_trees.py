class tree_node:
    def __init__(self, val, left = None, right = None):
        self.value = val
        self.right_child = right
        self.left_child = left

def bTree_search(node, searchVal):
	#Base case: if node matches or node doesn't exist return the current node
	if node.value == searchVal or node is None:
		return node
	#If search value greater than current node value recurse over right branch
	elif searchVal > node.value:
		if node.right_child:
			bTree_search(node.right_child, searchVal)
	#Else search value less than current node value recurse over left branch
	else: 
		if node.left_child:
			bTree_search(node.left_child, searchVal)

def bTree_insert(node, insertVal):
    if insertVal < node.value:
        if node.left_child is None:
            node.left_child = tree_node(insertVal)
        else:
            bTree_insert(node.left_child, insertVal)
        
    elif insertVal > node.value:
        if node.right_child is None:
            node.right_child = tree_node(insertVal)
        else:
            bTree_insert(node.right_child, insertVal)





node1 = tree_node("Moby Dick")
bTree_insert(node1, "Great Expectations")
bTree_insert(node1, "Robinson Crusoe")
bTree_insert(node1, "Alice in Wonderland")
bTree_insert(node1, "Lord of the Flies")
bTree_insert(node1, "Pride and Prejudice")
bTree_insert(node1, "The Odyssey")

def bTree_traverse_print(node):
    if node is None:
        return None
    else:
        bTree_traverse_print(node.left_child)
        print(node.value)
        bTree_traverse_print(node.right_child)

bTree_traverse_print(node1)

