#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

def get_jaccard_coefficient(graph,node1,node2):
    preds = nx.jaccard_coefficient(graph, [(node1, node2)])
    return list(preds)[0][2]

def get_shortest_path(graph,node1,node2):
    return nx.shortest_path_length(graph,node1,node2)

def get_pagerank(pr,node1,node2):
    return abs(pr[node1]-pr[node2])

lc = nx.read_pajek("lc.net")
graph = multigraph2graph(lc)

selection = [(u'Weichen Sun', u'Wei-Chen Sun'), (u'Jun-Nan Guo', u'Junnan Guo'), (u'Shigang Wang', u'Shi-gang Wang'), (u'Seyun Kim', u'Se-Yun Kim'), (u'Qingxin Xu', u'Qing-xin Xu'), (u'Mingchung Liu', u'Ming-Chung Liu'), (u'Liangjiang Zhou', u'Liang-jiang Zhou'), (u'Nae Zheng', u'Na-e Zheng'), (u'Ming-Yi Wang', u'Mingyi Wang'), (u'Gjalt de Jong', u'Gjalt De Jong'), (u'Xiao-Hong Wang', u'Xiaohong (Sophie) Wang'), (u'Xiao-Hong Wang', u'Xiaohong Wang'), (u'Xiaohong (Sophie) Wang', u'Xiaohong Wang'), (u'Jung-Uk Kim', u'Junguk Kim'), (u'Jung-Uk Kim', u'Jun-Guk Kim'), (u'Junguk Kim', u'Jun-Guk Kim'), (u'Mei-hua Chen', u'Mei-Hua Chen'), (u'Mei-hua Chen', u'Meihua Chen'), (u'Mei-Hua Chen', u'Meihua Chen'), (u'YanXia Zhang', u'Yanxia Zhang'), (u'YanXia Zhang', u'Yan-Xia Zhang'), (u'Yanxia Zhang', u'Yan-Xia Zhang'), (u'Hai-Yan Qiao', u'Haiyan Qiao'), (u'Hai-Yan Qiao', u'Hai-yan Qiao'), (u'Haiyan Qiao', u'Hai-yan Qiao'), (u'Yu-Ming Liu', u'Yu-ming Liu'), (u'Yu-Ming Liu', u'Yuming Liu'), (u'Yu-ming Liu', u'Yuming Liu'), (u'Hai-Lin Zhang', u'Hai-lin Zhang'), (u'Hai-Lin Zhang', u'Hailin Zhang'), (u'Hai-lin Zhang', u'Hailin Zhang'), (u'Mingli Song', u'Ming-Li Song'), (u'Mingli Song', u'Ming-li Song'), (u'Ming-Li Song', u'Ming-li Song'), (u'Xian-Fa Luo', u'Xianfa Luo'), (u'Xian-Fa Luo', u'XianFa Luo'), (u'Xianfa Luo', u'XianFa Luo'), (u'Yuan-yuan Zhang', u'Yuan-Yuan Zhang'), (u'Yuan-yuan Zhang', u'Yuanyuan Zhang'), (u'Yuan-Yuan Zhang', u'Yuanyuan Zhang'), (u'María de los Angeles Hernandez M.', u'Lenord Melvix J. S. M.'), (u'María de los Angeles Hernandez M.', u'Alejandro F. Lopez de Vergara M.'), (u'María de los Angeles Hernandez M.', u'Samimul Alam A. K. M.'), (u'Lenord Melvix J. S. M.', u'Alejandro F. Lopez de Vergara M.'), (u'Lenord Melvix J. S. M.', u'Samimul Alam A. K. M.'), (u'Alejandro F. Lopez de Vergara M.', u'Samimul Alam A. K. M.'), (u'HongJin Kim', u'Hong-jin Kim'), (u'HongJin Kim', u'Hongjin Kim'), (u'HongJin Kim', u'Hong-Jin Kim'), (u'Hong-jin Kim', u'Hongjin Kim'), (u'Hong-jin Kim', u'Hong-Jin Kim'), (u'Hongjin Kim', u'Hong-Jin Kim'), (u'Yi-jun Li', u'YiJun Li'), (u'Yi-jun Li', u'Yi-Jun Li'), (u'Yi-jun Li', u'Yijun Li'), (u'YiJun Li', u'Yi-Jun Li'), (u'YiJun Li', u'Yijun Li'), (u'Yi-Jun Li', u'Yijun Li'), (u'Frans C. T. van der Helm', u'Peer G. H. P. van der Helm'), (u'Frans C. T. van der Helm', u'A. W. C. van der Helm'), (u'Frans C. T. van der Helm', u'Aadjan J. C. van der Helm'), (u'Peer G. H. P. van der Helm', u'A. W. C. van der Helm'), (u'Peer G. H. P. van der Helm', u'Aadjan J. C. van der Helm'), (u'A. W. C. van der Helm', u'Aadjan J. C. van der Helm'), (u'M. S. S. N. Murty', u'P. S. R. C. Murty'), (u'M. S. S. N. Murty', u'S. A. V. Satya Murty'), (u'M. S. S. N. Murty', u'Neti V. L. Narasimha Murty'), (u'P. S. R. C. Murty', u'S. A. V. Satya Murty'), (u'P. S. R. C. Murty', u'Neti V. L. Narasimha Murty'), (u'S. A. V. Satya Murty', u'Neti V. L. Narasimha Murty'), (u'Yi-Ling Chen', u'YiLing Chen'), (u'Yi-Ling Chen', u'Yi-ling Chen'), (u'Yi-Ling Chen', u'Yiling Chen'), (u'YiLing Chen', u'Yi-ling Chen'), (u'YiLing Chen', u'Yiling Chen'), (u'Yi-ling Chen', u'Yiling Chen'), (u'Abdallah Ali Zainelabden Abdallah Ibrahim', u'B. S. KSM Kader Ibrahim'), (u'Abdallah Ali Zainelabden Abdallah Ibrahim', u'Ibrahim'), (u'Abdallah Ali Zainelabden Abdallah Ibrahim', u'Siti Nur Khadijah Aishah Ibrahim'), (u'B. S. KSM Kader Ibrahim', u'Ibrahim'), (u'B. S. KSM Kader Ibrahim', u'Siti Nur Khadijah Aishah Ibrahim'), (u'Ibrahim', u'Siti Nur Khadijah Aishah Ibrahim'), (u'Guohua Chen', u'Guo-hua Chen'), (u'Guohua Chen', u'Guo-Hua Chen'), (u'Guohua Chen', u'GuoHua Chen'), (u'Guo-hua Chen', u'Guo-Hua Chen'), (u'Guo-hua Chen', u'GuoHua Chen'), (u'Guo-Hua Chen', u'GuoHua Chen'), (u'Byung-Deok Chung', u'ByungDeok Chung'), (u'Byung-Deok Chung', u'Byung-deok Chung'), (u'Byung-Deok Chung', u'Byungdeok Chung'), (u'ByungDeok Chung', u'Byung-deok Chung'), (u'ByungDeok Chung', u'Byungdeok Chung'), (u'Byung-deok Chung', u'Byungdeok Chung'), (u'A. J. W. van den Boom', u'Anneliene A. L. F. M. van den Boom'), (u'A. J. W. van den Boom', u'Ton J. J. van den Boom'), (u'A. J. W. van den Boom', u'Henricus P. A. van den Boom'), (u'Anneliene A. L. F. M. van den Boom', u'Ton J. J. van den Boom'), (u'Anneliene A. L. F. M. van den Boom', u'Henricus P. A. van den Boom'), (u'Ton J. J. van den Boom', u'Henricus P. A. van den Boom'), (u'Lei Wang 0017', u'Lei Wang 0003'), (u'Lei Wang 0012', u'Lei Wang 0021'), (u'Lei Wang 0014', u'Lei Wang 0004'), (u'Lei Wang 0009', u'Lei Wang 0006'), (u'Lei Wang 0022', u'Lei Wang 0020'), (u'Lei Wang 0013', u'Lei Wang 0001'), (u'Lei Wang 0014', u'Lei Wang 0007'), (u'Lei Wang 0005', u'Lei Wang 0003'), (u'Lei Wang 0001', u'Lei Wang 0025'), (u'Lei Wang 0017', u'Lei Wang 0020'), (u'Lei Zhang 0009', u'Lei Zhang 0010'), (u'Lei Zhang 0001', u'Lei Zhang 0014'), (u'Lei Zhang 0005', u'Lei Zhang 0008'), (u'Lei Zhang 0012', u'Lei Zhang 0031'), (u'Lei Zhang 0031', u'Lei Zhang 0030'), (u'Lei Zhang 0012', u'Lei Zhang 0028'), (u'Lei Zhang 0002', u'Lei Zhang 0016'), (u'Lei Zhang 0003', u'Lei Zhang 0018'), (u'Lei Zhang 0029', u'Lei Zhang 0034'), (u'Lei Zhang 0002', u'Lei Zhang 0027'), (u'Li Li 0009', u'Li Li 0005'), (u'Li Li 0022', u'Li Li 0003'), (u'Li Li 0022', u'Li Li 0009'), (u'Li Li 0025', u'Li Li 0009'), (u'Li Li 0015', u'Li Li 0005'), (u'Li Li 0005', u'Li Li 0003'), (u'Li Li 0010', u'Li Li 0023'), (u'Li Li 0023', u'Li Li 0015'), (u'Li Li 0028', u'Li Li 0016'), (u'Li Li 0020', u'Li Li 0021'), (u'Ming Li 0022', u'Ming Li 0002'), (u'Ming Li 0018', u'Ming Li 0021'), (u'Ming Li 0019', u'Ming Li 0024'), (u'Ming Li 0008', u'Ming Li 0024'), (u'Ming Li 0006', u'Ming Li 0009'), (u'Ming Li 0013', u'Ming Li 0023'), (u'Ming Li 0027', u'Ming Li 0022'), (u'Ming Li 0010', u'Ming Li 0021'), (u'Ming Li 0007', u'Ming Li 0026'), (u'Ming Li 0014', u'Ming Li 0018'), (u'Wei Li 0005', u'Wei Li 0011'), (u'Wei Li 0013', u'Wei Li 0053'), (u'Wei Li 0025', u'Wei Li 0019'), (u'Wei Li 0058', u'Wei Li'), (u'Wei Li 0044', u'Wei Li 0038'), (u'Wei Li 0015', u'Wei Li 0053'), (u'Wei Li 0018', u'Wei Li 0055'), (u'Wei Li 0002', u'Wei Li 0004'), (u'Wei Li 0030', u'Wei Li 0006'), (u'Wei Li 0054', u'Wei Li 0011'), (u'Wei Wang 0007', u'Wei Wang 0015'), (u'Wei Wang 0017', u'Wei Wang 0015'), (u'Wei Wang 0033', u'Wei Wang 0006'), (u'Wei Wang 0047', u'Wei Wang 0021'), (u'Wei Wang 0039', u'Wei Wang 0008'), (u'Wei Wang 0037', u'Wei Wang 0031'), (u'Wei Wang 0032', u'Wei Wang 0008'), (u'Wei Wang', u'Wei Wang 0028'), (u'Wei Wang 0030', u'Wei Wang 0009'), (u'Wei Wang 0042', u'Wei Wang 0052'), (u'Wei Zhang 0037', u'Wei Zhang 0006'), (u'Wei Zhang 0011', u'Wei Zhang 0007'), (u'Wei Zhang 0026', u'Wei Zhang 0004'), (u'Wei Zhang 0006', u'Wei Zhang 0044'), (u'Wei Zhang 0048', u'Wei Zhang 0025'), (u'Wei Zhang 0039', u'Wei Zhang 0014'), (u'Wei Zhang 0029', u'Wei Zhang 0008'), (u'Wei Zhang 0031', u'Wei Zhang 0008'), (u'Wei Zhang 0003', u'Wei Zhang 0044'), (u'Wei Zhang 0050', u'Wei Zhang 0018'), (u'Yang Liu 0031', u'Yang Liu 0024'), (u'Yang Liu 0002', u'Yang Liu 0007'), (u'Yang Liu 0013', u'Yang Liu 0002'), (u'Yang Liu 0024', u'Yang Liu 0011'), (u'Yang Liu 0025', u'Yang Liu 0007'), (u'Yang Liu 0021', u'Yang Liu 0006'), (u'Yang Liu 0011', u'Yang Liu 0016'), (u'Yang Liu 0022', u'Yang Liu 0026'), (u'Yang Liu 0031', u'Yang Liu 0020'), (u'Yang Liu 0030', u'Yang Liu 0028'), (u'Yu Wang 0030', u'Yu Wang 0040'), (u'Yu Wang 0022', u'Yu Wang 0011'), (u'Yu Wang 0017', u'Yu Wang 0011'), (u'Yu Wang 0005', u'Yu Wang 0018'), (u'Yu Wang 0037', u'Yu Wang 0018'), (u'Yu Wang 0033', u'Yu Wang 0021'), (u'Yu Wang 0003', u'Yu Wang 0012'), (u'Yu Wang 0014', u'Yu Wang 0013'), (u'Yu Wang 0015', u'Yu Wang 0012'), (u'Yu Wang 0003', u'Yu Wang 0032'), (u'Zhi Li 0013', u'Zhi Li 0035'), (u'Zhi Li 0001', u'Zhi Li 0035'), (u'Zhi Li 0012', u'Zhi Li 0010'), (u'Zhi Li 0022', u'Zhi Li 0027'), (u'Zhi Li 0004', u'Zhi Li 0003'), (u'Zhi Li 0008', u'Zhi Li 0021'), (u'Zhi Li 0007', u'Zhi Li 0030'), (u'Zhi Li 0006', u'Zhi Li 0030'), (u'Zhi Li 0027', u'Zhi Li 0018'), (u'Zhi Li 0025', u'Zhi Li 0030')]

f = open("SP.csv", 'w')
f.write('Name1,Name2,ShortestPath\n')
for name in selection:
    name1 = name[0]
    name2 = name[1]
    line = name1.encode('utf-8')+","+name2.encode('utf-8')+",F,"
    if name1 in graph and name2 in graph and nx.has_path(graph,name1,name2):
        spath = get_shortest_path(graph,name1,name2)
        line = line + str(spath)
    else:
        line = line+"0"
    f.write(line+"\n")
f.close()

f = open("Jaccard.csv", 'w')
f.write('Name1,Name2,JaccardCoefficient\n')
for name in selection:
    name1 = name[0]
    name2 = name[1]
    line = name1.encode('utf-8')+","+name2.encode('utf-8')+",F,"
    if name1 in graph and name2 in graph and nx.has_path(graph,name1,name2):
        jaccard = get_jaccard_coefficient(graph,name1,name2)
        line = line + str(jaccard)
    else:
        line = line+"0"
    f.write(line+"\n")
f.close()

pr = nx.pagerank(graph)
f = open("PR.csv", 'w')
f.write('Name1,Name2,PageRank\n')
for name in selection:
    name1 = name[0]
    name2 = name[1]
    line = name1.encode('utf-8')+","+name2.encode('utf-8')+",F,"
    if name1 in graph and name2 in graph and nx.has_path(graph,name1,name2):
        pagerank = get_pagerank(pr,name1,name2)
        line = line + str(pagerank)
    else:
        line = line+"10"
    f.write(line+"\n")
f.close()
