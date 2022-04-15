class node:
    def __init__(self, node_val = None):   
        self.node_val = node_val
        self.next_node = None

class linked_list:
    def __init__(self):
        self.first_node = None


list_1 = linked_list()
list_1.first_node = node('this is first_node')

node_2 = node(('this is second node'))
list_1.first_node.next_node = node_2

node_3 = node('this is third node')
node_2.next_node = node_3

print(list_1.first_node.node_val)
print(list_1.first_node.next_node.node_val)
print(list_1.first_node.next_node.next_node.node_val)



