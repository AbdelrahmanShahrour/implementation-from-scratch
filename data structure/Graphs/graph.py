class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list: # remember you cant use k, v for a dict
            print(vertex, ':', self.adj_list[vertex])

    # Creates new vertex, t/c - O(1)
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys(): # to avoid duplicate entries
            self.adj_list[vertex] = []
            return True
        return False

    # Creates a connection b/w two vertices, t/c - O(1)
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): # checking node exists
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    # removes the connection, t/c - O(|E|) # edge, we have to iterate a list to find element
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): # check node exists
            try: # for non exist connection
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    # removes node and it's all connection, t/c - O(|V| + |E|) check every lists
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys(): # check exists
            # this returns the connection with other nodes
            for other_vertex in self.adj_list[vertex]:
                # On connected nodes remove value from list
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex] # deletes entire k, v pair
            return True
        return False