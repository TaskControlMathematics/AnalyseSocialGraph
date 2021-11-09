import networkx
import numpy as np
def cluster_cof (graf):
    claster_list=networkx.clustering(graf)
    clasters=claster_list.values()
    return sum(clasters)/graf.number_of_nodes()

def pr(spisok):
    n = len(spisok)
    for i in range(n):
        ver = spisok[i][1]
        if not ([ver,spisok[i][0]] in spisok):
            spisok.append([ver,spisok[i][0]])
    spisok.sort()
    return spisok
            
def list_to_mat(spisok):
    all_nodes = []
    for i in range(len(spisok)):
        all_nodes.append(spisok[i][0])
    unic_nodes = list(set(all_nodes))
    n= len(unic_nodes)
    A = [[0] * n for i in range(n)]
    for i in range(len(spisok)):
        k = spisok[i][0]
        j = spisok[i][1]
        A[k][j] = 1
    return A

def to_list_from_file(filename):
    file = open(filename, 'r')
    fr=[]
    for (i, line) in enumerate(file):
        for (j, bl) in enumerate(line[:-1].split(';')):
            if bl == '1':
                fr.append([i,j])
    file.close()
    return fr

def get_list_smegn(spisok,ver):
    smegn = []
    for i in range(len(spisok)):
        if spisok[i][0] == ver:
            smegn.append(spisok[i][1])
    return smegn

def get_num_of_edjes(spisok,ver):
    count = 0
    matr = list_to_mat(spisok)
    sp = get_list_smegn(spisok,ver)
    for i in range(len(sp)):
        for j in range(len(sp)):
            if matr[sp[i]][sp[j]] == 1 and matr[sp[j]][sp[i]] == 1:
                count+=0.5
    return count
 
def node_coef(spisok,ver):
    e = get_num_of_edjes(spisok,ver)
    k = len(get_list_smegn(spisok,ver))
    if k == 1:
        return 0
    cl = 2*e/(k*(k-1))
    return cl

def coef_clust(spisok):
    coef = 0
    all_nodes = []
    for i in range(len(spisok)):
        all_nodes.append(spisok[i][0])
    unic_nodes = list(set(all_nodes))
    for i in range(len(unic_nodes)):
        cl = node_coef(spisok, unic_nodes[i])
        coef+=cl
    return coef/(len(unic_nodes))

def gen_list_graf(p, col_nodes):
    edges = []
    for i in range(col_nodes):
        for j in range(i,col_nodes):
            if np.random.rand() < p and i!=j:
                edges.append([i,j])
    return edges

#friends
A = pr(to_list_from_file('friends.csv'))
print('friends by hands', coef_clust(A))

fr_graph=networkx.read_edgelist('friends.txt') 
fr_cl=cluster_cof(fr_graph)
print('friends by netwokx', fr_cl)

p=np.log(19)/18
print('p(n) = ', p)

A = pr(gen_list_graf(p,19))
print('random clustering for friends ',coef_clust(A))

#date_born
A = pr(to_list_from_file('births.csv'))
print('births by hands', coef_clust(A))

dr_graph=networkx.read_edgelist('births.txt') 
dr_cl=cluster_cof(dr_graph)
print('births by netwokx', dr_cl)

p=np.log(19)/18
print('p(n) = ', p)

A = pr(gen_list_graf(p,19))
print('random clustering for births ',coef_clust(A))

#random graph
f=open('Wiki-Vote.txt','r')
wiki = []
for line in f:
    wiki.append([int(line.replace('\t',' ').replace('\n','').split(' ')[0]), int(line.replace('\t',' ').replace('\n','').split(' ')[1])])
wiki=pr(wiki)
print('wiki-vote by hands', coef_clust(wiki))

wiki_graph=networkx.read_edgelist('Wiki-Vote.txt') 
wiki_cl=cluster_cof(wiki_graph)
print('wiki by netwokx', wiki_cl)

p=np.log(7115)/7114
print('p(n) = ', p)

A = pr(gen_list_graf(p,7115))
print('random clustering for wiki ',coef_clust(A))