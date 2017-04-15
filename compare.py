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

nodes = graph.nodes()
for i in range(0,len(graph)-1):
    for j in range(i+1,len(graph)):
        name1 = nodes[i]
        name2 = nodes[j]
        if (name1 == name or name1[:-5].strip() == name) and (name2 == name or name2[:-5].strip() == name):
            print name1,name2
            if nx.has_path(graph,name1,name2):
                print "Jaccard coef: ",get_jaccard_coefficient(graph,name1,name2)
                print "Shortest path: ",get_shortest_path(graph,name1,name2)
            else:
                print "not connected"
            print "---------------------------"
