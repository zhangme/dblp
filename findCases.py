import networkx as nx
import random

name_list = ["Lei Wang","Lei Zhang","Li Li","Ming Li","Wei Li","Wei Wang","Wei Zhang","Yang Liu","Yu Wang","Zhi Li"]
all_pairs = []
for name in name_list:
    graph = nx.read_pajek(name+".net")
    nodes = graph.nodes()
    name_pair = []
    for i in range(0,len(graph)-1):
        for j in range(i+1,len(graph)):
            name1 = nodes[i]
            name2 = nodes[j]
            if (name1 == name or name1[:-5].strip() == name) and (name2 == name or name2[:-5].strip() == name):
                name_pair.append((name1,name2))
    selection = random.sample(range(0, len(name_pair)), 10)
    selected = list(name_pair[i] for i in selection)
    all_pairs+=selected

print all_pairs
