import networkx as nx

dblp = nx.read_pajek("dblp.net")
lc = sorted(nx.connected_component_subgraphs(dblp), key = len, reverse=True)[0]
nx.write_pajek(lc, "lc.net")
