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

    def dfs(self, visited = set(), path = ""):
        # if path == None:
        #     path = []
        # path.append(self.value)
        path = path + self.value +","
        print("current path: ", path)
        visited.add(self)
        print("add vertex: ",self.value)
        for adjacent in self.adjacent_vertices:
            if adjacent and adjacent not in visited:
                adjacent.dfs(visited, path)

            
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

path = joe.dfs()
#print(path)

#for vertex in irina.adjacent_vertices:
 #   print(vertex.value)



# for vertex in joe.adjacent_vertices:
#     print(vertex.value, " is Joe's friend")

# for vertex in bob.adjacent_vertices:
#     print(vertex.value, " is Bob's friend")




   