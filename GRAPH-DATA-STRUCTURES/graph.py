from pickle import TRUE


class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent(self, neighbor_vertex):
        self.adjacent_vertices.append(neighbor_vertex)
   
    def undirected_add_adjacent(self, neighbor_vertex):
        if neighbor_vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(neighbor_vertex)
            neighbor_vertex.undirected_add_adjacent(self)

    def dfs_traverse(self, visited = set(), path = ""):
        # if path == None:
        #     path = []
        # path.append(self.value)
        path = path + self.value +","
        print("current path: ", path)
        visited.add(self)
        print("add vertex: ",self.value)
        for adjacent in self.adjacent_vertices:
            if adjacent and adjacent not in visited:
                adjacent.dfs_traverse(visited, path)
    
    def dfs_search(self, searchValue, visited = set(), path = ""):
        path = path + self.value +","
        print("current path: ", path)
        visited.add(self)
        print("add vertex: ",self.value)
        if searchValue == self.value:
            print("Value found")
            return self
        for adjacent in self.adjacent_vertices:
            if adjacent not in visited:
                if adjacent.value == searchValue:
                    print("Value found")
                    path = path + adjacent.value
                    print("current path: ", path)
                    return adjacent
                vertex_search = adjacent.dfs_search(searchValue, visited, path)
                
                if vertex_search:
                    return vertex_search
        return None

            
joe = Vertex("Joe")
bob = Vertex("Bob")
candy = Vertex("Candy")
derek = Vertex("Derek")
elaine = Vertex("Elaine")
fred = Vertex("Fred")
gina = Vertex("Gina")
helen = Vertex("Helen")
irina = Vertex("Irina")

joe.undirected_add_adjacent(bob)
joe.undirected_add_adjacent(candy)
joe.undirected_add_adjacent(derek)
joe.undirected_add_adjacent(elaine)

bob.undirected_add_adjacent(fred)
fred.undirected_add_adjacent(helen)
helen.undirected_add_adjacent(candy)

derek.undirected_add_adjacent(elaine)
derek.undirected_add_adjacent(gina)


gina.undirected_add_adjacent(irina)

path = joe.dfs_traverse()
joe.dfs_search("Helen")
joe.dfs_search("John")
#print(path)

#for vertex in irina.adjacent_vertices:
 #   print(vertex.value)



# for vertex in joe.adjacent_vertices:
#     print(vertex.value, " is Joe's friend")

# for vertex in bob.adjacent_vertices:
#     print(vertex.value, " is Bob's friend")




   