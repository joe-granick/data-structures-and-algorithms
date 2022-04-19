from pickle import LIST


class node:
    def __init__(self, node_val = None):   
        self.node_val = node_val
        self.next_node = None
        self.previous_node = None

class linked_list:
    def __init__(self):
        self.first_node = None
    def read(self, index):
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            current_node = current_node.next_node
            current_index+=1
        return current_node.node_val
    def search(self, val):
        current_node = self.first_node
        index = 0
        while current_node:
            if current_node.node_val == val:
                return index
            current_node = current_node.next_node
            index+=1
        return None
    def insert(self, val, index=0):
        current_node = self.first_node
        new_node = node(val)
        current_index = 0
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
        else:
            while current_index < index-1:
                current_node = current_node.next_node
                current_index+=1
            next_next_node = current_node.next_node
            current_node.next_node = new_node
            current_node.next_node.next_node = next_next_node
    def delete(self, index=0):
        current_node = self.first_node
        current_index = 0
        if index == 0:
            self.first_node = self.first_node.next_node
        else:
            while current_index < index-1:
                current_node = current_node.next_node
                current_index +=1
            new_next_node = current_node.next_node.next_node
            current_node.next_node = new_next_node
    def print_list(self):
        current_node = self.first_node
        node_index = 0
        while current_node:
            val = current_node.node_val
            print("Node ", node_index ,":", val)
            node_index+=1
            current_node = current_node.next_node
    def last_node(self):
        current_node = self.first_node
        while  current_node.next_node:
            current_node = current_node.next_node
        return current_node
    def reverse_list(self):
        current_node = self.first_node
        insert_node = current_node.next_node
        current_node.next_node.delete()
        self.insert(insert_node.node_val, 0)
        pass

class double_linked_list:
    def __init__(self):
        self.first_node = None
        self.last_node = None
    
    def read(self, index):
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            current_node = current_node.next_node
            current_index+=1
        return current_node.node_val
    
    def search(self, val):
        current_node = self.first_node
        index = 0
        while current_node:
            if current_node.node_val == val:
                return index
            current_node = current_node.next_node
            index+=1
        return None
    
    def insert(self, val, index):
        current_node = self.first_node
        new_node = node(val)
        current_index = 0
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            #self.first_node.next_node = current_node  
        else:
            while current_index < index-1:
                current_node = current_node.next_node
                current_index+=1
            next_next_node = current_node.next_node
            current_node.next_node = new_node
            current_node.next_node.next_node = next_next_node
    
    def insert_at_end(self, val):
        new_node = node(val)
        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node

    def delete(self, index):
        current_node = self.first_node
        current_index = 0
        if index == 0:
            self.first_node = self.first_node.next_node
        else:
            while current_index < index-1:
                current_node = current_node.next_node
                current_index +=1
            new_next_node = current_node.next_node.next_node
            current_node.next_node = new_next_node
    
    def print_list(self):
        current_node = self.first_node
        node_index = 0
        while current_node:
            val = current_node.node_val
            print("Node ", node_index ,":", val)
            node_index+=1
            current_node = current_node.next_node
    



list_1 = linked_list()
list_1.first_node = node('this is first_node')

node_2 = node(('this is second node'))
list_1.first_node.next_node = node_2

node_3 = node('this is third node')
node_2.next_node = node_3

print(list_1.first_node.node_val)
print(list_1.first_node.next_node.node_val)
print(list_1.first_node.next_node.next_node.node_val)
print(list_1.read(0))


print(list_1.search('this is first_node'))
print(list_1.search('this is second node'))
print(list_1.search('this is third node'))
print(list_1.search('this is first node'))

list_1.print_list()
print("Insert index 0")
list_1.insert("this is new first node", 0)
list_1.print_list()
print("Insert index 1")
list_1.insert("this is new second node", 1)
list_1.print_list()
print("Insert index 5")
list_1.insert("this is new last node", 5)
list_1.print_list()

#list_1.insert("this is extra last node", 10)
#print(list_1.read(6))

list_1.print_list()
print("Delete index 0")
list_1.delete(0)
list_1.print_list()
print("Delete index 4")
list_1.delete(4)
#print(list_1.read(4))
list_1.print_list()
print(list_1.last_node().node_val)

list_2 = double_linked_list()

list_2.insert_at_end("This is first value in double linked list")
list_2.print_list()

list_2.insert_at_end("This is second value in double linked list")
list_2.print_list()

list_2.insert_at_end("This is third value in double linked list")
list_2.print_list()

#print(list_2.read(0))
print(list_2.first_node.node_val)
print(list_2.last_node.node_val)
print(list_2.last_node.previous_node.node_val)









