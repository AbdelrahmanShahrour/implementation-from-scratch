import graph

my_graph = graph.Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')

#my_graph.remove_edge('A', 'B')
#my_graph.remove_edge('A', 'D')

my_graph.remove_vertex('D')
my_graph.print_graph()