import networkx as nx

graph = nx.read_pajek("Meng Zhang.net")
name = "Meng Zhang"
def get_jaccard_coefficient(graph,node1,node2):
    preds = nx.jaccard_coefficient(graph, [(node1, node2)])
    return list(preds)[0][2]

def get_shortest_path(graph,node1,node2):
    return nx.shortest_path_length(graph,node1,node2)


for node in graph:
    if node[-4:].isdigit() and node[:-5] == name:
        print name,node
        print "Jaccard coef: ",get_jaccard_coefficient(graph,name,node)
        print "Shortest path: ",get_shortest_path(graph,name,node)
        print "---------------------------"
