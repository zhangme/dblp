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

lc = nx.read_pajek("lc.net")

similar_names = {}
all_nodes = lc.nodes()
for node in all_nodes:
    if node[-4:].isdigit() and len(node)>4:
        name = node[:-5].strip()
        if name in all_nodes:
            if name in similar_names:
                similar_names[name][node] = all_nodes.index(node)
            else:
                similar_names[name] = {name:all_nodes.index(name),node:all_nodes.index(node)}
count_list = (len(key) for key in similar_names.values())
top_10 = sorted(count_list,reverse=True)[9]
selection = [key for key,value in similar_names.items() if len(value) >= top_10]
print "number of similar names: ",len(similar_names.keys())
print "highest count: ",max(count_list)

for case in selection:
    graph = nx.ego_graph(lc,case)
    for pair in similar_names[case]:
        subgraph = nx.ego_graph(lc,pair)
        graph = nx.compose(graph,subgraph)
    graph = multigraph2graph(graph)
    nx.write_pajek(graph, str(case)+".net")
