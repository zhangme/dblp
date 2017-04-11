from lxml import etree
import networkx as nx

source = 'dblp.xml'
dtd = etree.DTD(file='dblp.dtd') #need to change second line in dblp.xml

author=[]
title=[]
G=nx.Graph()

for event, element in etree.iterparse(source, load_dtd=True):
    if 	element.getchildren() and element.tag!="dblp" and element.tag!="www":
        if len(author)>1:
            for person in author:
                if G.has_node(person):
                    temp = G.node[person]["title"] + title
                    G.add_node(person,title=temp)
                else:
                    G.add_node(person,title=title)
            for i in range(0,len(author)-1):
                for j in range(i+1,len(author)):
                    p1,p2=author[i],author[j]
                    if G.has_edge(p1,p2):
                        G[p1][p2]['weight']+=1
                    else:
                        G.add_edge(p1,p2,weight=1)
        elif len(author)==1:
            if G.has_node(author[0]):
                title = G.node[author[0]]["title"] + title
            G.add_node(author[0],title=title)
        author=[]
        title=[]
        continue
    if element.tag=="author" or element.tag=="editor":
        name = element.text.replace("\"","")
        if len(name.split())==1:
            name="\""+name+"\""
        author.append(name)
    if element.tag=="title" or element.tag=="booktitle" or element.tag=="journal":
        title.append(element.text.replace("\"","").replace("\'",""))

    element.clear()

nx.write_pajek(G, "dblp.net")

lc = sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]
nx.write_pajek(lc, "lc.net")
