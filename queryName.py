from lxml import etree
import networkx as nx

source = 'dblp.xml'
dtd = etree.DTD(file='dblp.dtd')

author=[]
G=nx.Graph()

for event, element in etree.iterparse(source, load_dtd=True):
    if 	element.getchildren() and element.tag!="dblp":
        if len(author)>1:
            for item in author:
                G.add_node(name)
            for i in range(0,len(author)-1):
                for j in range(i+1,len(author)):
                    p1,p2=author[i],author[j]
                    if G.has_edge(p1,p2):
                        G[p1][p2]['weight']+=1
                    else:
                        G.add_edge(p1,p2,weight=1)
        author=[]
        continue
    if element.tag=="author" or element.tag=="editor":
        name = element.text.replace("\"","")
        if len(name.split())==1:
            name="\""+name+"\""
        author.append(name)
    element.clear()

nx.write_pajek(G, "dblp.net")
#nx.write_gml(G, "dblp.gml")
