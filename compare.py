import networkx as nx

def multigraph2graph(graph):
    G = nx.Graph()
    for u,v,data in graph.edges_iter(data=True):
        w = data['weight'] if 'weight' in data else 1.0
        if G.has_edge(u,v):
            continue
        else:
            G.add_edge(u, v, weight=w)
    return G

def get_jaccard_coefficient(graph,node1,node2):
    if nx.has_path(graph,node1,node2):
        preds = nx.jaccard_coefficient(graph, [(node1, node2)])
        return list(preds)[0][2]
    else:
        return "nodes not connected"

def get_shortest_path(graph,node1,node2):
    if nx.has_path(graph,node1,node2):
        return nx.shortest_path_length(graph,node1,node2)
    else:
        return "nodes not connected"


name = "Li Li"
graph = nx.read_pajek(name+".net")
graph = multigraph2graph(graph)

for node in graph:
    if node[-4:].isdigit() and node[:-5].strip() == name:
        print name,node
        if nx.has_path(graph,node,name):
            print "Jaccard coef: ",get_jaccard_coefficient(graph,name,node)
            print "Shortest path: ",get_shortest_path(graph,name,node)
        else:
            print "not connected"
        print "---------------------------"
