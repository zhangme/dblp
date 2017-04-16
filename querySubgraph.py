import networkx as nx

lc = nx.read_pajek("lc.net")

similar_names = {}
all_nodes = lc.nodes()
for node in all_nodes:
    if node[-4:].isdigit() and len(node)>4:
        name = node[:-5].strip()
        if name in all_nodes:
            if name in similar_names:
                similar_names[name][node] = graph.node[node]["id"]
            else:
                similar_names[name] = {name:graph.node[name]["id"],node:graph.node[node]["id"]}
count_list = (len(key) for key in similar_names.values())
top_10 = sorted(count_list,reverse=True)[9]
selection = [key for key,value in similar_names.items() if len(value) >= top_10]
print "number of similar names: ",len(similar_names.keys()) #1397
c = (len(key) for key in similar_names.values())
top = sorted(c,reverse=True)[:10]
s = [(key,len(value)) for key,value in similar_names.items() if len(value) in top]

for case in selection:
    graph = nx.ego_graph(lc,case)
    for pair in similar_names[case]:
        subgraph = nx.ego_graph(lc,pair)
        graph = nx.compose(graph,subgraph)
    nx.write_pajek(graph, str(case)+".net")
