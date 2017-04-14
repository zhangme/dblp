import networkx as nx

g = nx.read_pajek("lc.net")

def get_jaccard_coefficient(graph,node1,node2):
    preds = nx.jaccard_coefficient(graph, [(node1, node2)])
    return list(preds)[0][2]

def get_shortest_path(graph,node1,node2):
    return nx.shortest_path_length(graph,node1,node2)
