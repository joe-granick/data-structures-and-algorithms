from decimal import ROUND_DOWN, ROUND_FLOOR


class heap:
    def __init__(self):
        self.data = []

    def root_node(self):
        return self.data[0]

    def last_node(self):
        return self.data[-1]
    
    def parent_index(self, index):
        return (index-1)/2

    def left_child_index(self, index):
        return (index*2)+1

    def right_child_index(self, index):
        return (index*2)+2

    def insert(self, val):
        self.data.append(val)
        insert_index = len(self.data)-1
        pass

    def trickle_up(self):
        pass

    def delete(self):
        self.root_node = self.last_node
        self.last_node = None

    def has_greater_child(self):
        pass

    def greater_child_index(self):
        pass

 


