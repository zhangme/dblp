import networkx as nx

dblp = nx.read_pajek("dblp.net")

#print "nodes: ", dblp.number_of_nodes() #1808650
#print "edges: ", dblp.number_of_edges() #8509033
#print "density: ", nx.density(dblp) #5.20237169758e-06
#print "average degree: ",sum(dblp.degree().values())/float(len(dblp)) #9.40926436845

#print "number of components: ", nx.number_connected_components(dblp) #54502
#largest component
#lc = sorted(nx.connected_component_subgraphs(dblp), key = len, reverse=True)[0]
#largest component % to whole graph
#print float(nx.number_of_nodes(lc))/nx.number_of_nodes(dblp)
#largest component diameter
#print nx.diameter(lc)
#largest componenet average shortest path
#print nx.average_shortest_path_length(lc)




#######################Extra###############################

# print "degree_centrality: ", nx.degree_centrality(dblp)
# print "closeness_centrality: ", nx.closeness_centrality(dblp)
# print "betweenness_centrality: ", nx.closeness_centrality(dblp)

# import matplotlib.pyplot as plt

# nx.draw(dblp)
# nx.draw_networkx(dblp, with_labels=True)
# plt.show()
