import networkx as nx

dblp = nx.read_pajek("dblp.net")

# print "number of components: ", nx.number_connected_components(G) #121476

lc = nx.read_pajek("lc.net")

# print "nodes: ", lc.number_of_nodes() #1329526
# print "edges: ", lc.number_of_edges() #6224694
# print "density: ", nx.density(lc) #7.04295088224e-06
# print "average degree: ",sum(lc.degree().values())/float(len(lc)) #9.36377927171
# print "percent to whole graph",float(nx.number_of_nodes(lc))/nx.number_of_nodes(G) #0.857090731868



#######################Extra###############################

# print "diameter",nx.diameter(lc)
# print "average shortest path",nx.average_shortest_path_length(lc)

# print "degree_centrality: ", nx.degree_centrality(dblp)
# print "closeness_centrality: ", nx.closeness_centrality(dblp)
# print "betweenness_centrality: ", nx.closeness_centrality(dblp)

# import matplotlib.pyplot as plt

# nx.draw(dblp)
# nx.draw_networkx(dblp, with_labels=True)
# plt.show()
