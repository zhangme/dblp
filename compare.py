import networkx as nx
from numpy import *

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
    preds = nx.jaccard_coefficient(graph, [(node1, node2)])
    return list(preds)[0][2]

def get_shortest_path(graph,node1,node2):
    return nx.shortest_path_length(graph,node1,node2)

def get_pagerank(pr,node1,node2):
    return abs(pr[node1]-pr[node2])

def get_hitting_time(graph,node1,node2):
    node_list = graph.nodes()
    node1_index = node_list.index(node1)
    node2_index = node_list.index(node2)
    hit_index = (node1_index,node2_index)
    A = nx.to_numpy_matrix(graph,weight=None,multigraph_weight=min)
    A = squeeze(asarray(A))
    A[hit_index[1],:] = 0
    A[hit_index[1],hit_index[1]] = 1
    A = (A.T/A.sum(axis=1)).T
    B = A.copy()
    X = []
    tar_val = B[hit_index]
    i = 0
    while tar_val < 0.99:
        tar_val = B[hit_index]
        X.append(tar_val)
        B = dot(B,A)
        i+=1
    Y = X[:]
    Y.append(Y[-1])
    Z = []
    for i in range(len(X)):
        Z.append((Y[i+1]-X[i])*i)
    expectation = sum(Z)
    return (round(expectation),i)

name = "Li Li"
graph = nx.read_pajek(name+".net")
graph = multigraph2graph(graph)
nodes = graph.nodes()

name1 = "Li Li"
name2 = "Li Li 0001"
print get_hitting_time(graph,name1,name2)

# name_list = ["Lei Wang","Lei Zhang","Li Li","Ming Li","Wei Li","Wei Wang","Wei Zhang","Yang Liu","Yu Wang","Zhi Li"]
# for name in name_list:
#     graph = nx.read_pajek(name+".net")
#     graph = multigraph2graph(graph)
#     nodes = graph.nodes()
#     pr = nx.pagerank(graph)
#     f = open(name+".csv", 'w')
#     f.write('Name1,Name2,GroundTruth,JaccardCoefficient,ShortestPath,PageRank,Connected\n')
#     for i in range(0,len(graph)-1):
#         for j in range(i+1,len(graph)):
#             name1 = nodes[i]
#             name2 = nodes[j]
#             if (name1 == name or name1[:-5].strip() == name) and (name2 == name or name2[:-5].strip() == name):
#                 line = name1+","+name2+",F,"
#                 if nx.has_path(graph,name1,name2):
#                     jaccard = get_jaccard_coefficient(graph,name1,name2)
#                     spath = get_shortest_path(graph,name1,name2)
#                     pagerank = get_pagerank(pr,name1,name2)
#                     line = line + str(jaccard) + "," + str(spath) + "," + str(pagerank) + ",T"
#                 else:
#                     line = line+",,,F"
#                 f.write(line+"\n")
#     f.close()
