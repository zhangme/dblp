import networkx as nx

dblp = nx.read_pajek("dblp.net")

#print "nodes: ", dblp.number_of_nodes() #1896883
#print "edges: ", dblp.number_of_edges() #8488316
#print "average clustering coefficient: ", nx.density(dblp)


# average degree

# Largest component (how big is it %age wise)
#
# Diameter
#
# Average shortest path




# print "degree_centrality: ", nx.degree_centrality(dblp)
# print "closeness_centrality: ", nx.closeness_centrality(dblp)
# print "betweenness_centrality: ", nx.closeness_centrality(dblp)

# import matplotlib.pyplot as plt

# nx.draw(dblp)
# nx.draw_networkx(dblp, with_labels=True)
# plt.show()
