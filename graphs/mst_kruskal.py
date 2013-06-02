#!/usr/bin/python
from pprint import pprint

# Minimum Spanning Tree
# Kruskal's Algorithm

#    for each vertex v in G.V
#       MAKE-SET(v)

#   A = {}

#   sort edges in non-decreasing order
#   for each edge (u,v) do
#       if FIND-SET(u) != FIND-SET(v) do
#           A = A U {(u,v)}
#           UNION(u, v)
#   return A


gset = {}

def union_set(u, v):
    global gset
    parent_u = gset[u]
    parent_v = gset[v]
    for vertex in gset.keys():
        if gset[vertex] == parent_u: 
            gset[vertex] = parent_v

def make_set(v):
    global gset
    gset[v] = v

def kruskal(G):
    global gset
    for v in G['vertices']:
        make_set(v)

    #pprint(gset)

    A = []  # minimum spanning tree

    edges = list(G['edges'])

    edges.sort()
    for i in range(len(edges)):
        e = edges[i]
        w, u, v = e
        if gset[u] != gset[v]:
            A.append(e)
            union_set(u, v)
            #print 'appending ' + str(e)
            #pprint(gset)
            #ri = raw_input()
    
    print "\nEdges that form the Minimum Spanning Tree : \n" 
    pprint(A)

def generate_graph():

    G = {
        'vertices' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
        'edges' : set([
            (4, 'a', 'b'),
            (8, 'a', 'h'),
            (4, 'b', 'a'),
            (8, 'b', 'c'),
            (11, 'b', 'h'),
            (8, 'c', 'b'),
            (7, 'c', 'd'),
            (4, 'c', 'f'),
            (2, 'c', 'i'),
            (7, 'd', 'c'),
            (7, 'd', 'e'),
            (14, 'd', 'f'),
            (9, 'e', 'd'),
            (10, 'e', 'f'),
            (4, 'f', 'c'),
            (14, 'f', 'd'),
            (10, 'f', 'e'),
            (2, 'f', 'g'),
            (1, 'g', 'h'),
            (6, 'g', 'i'),
            (8, 'h', 'a'),
            (11, 'h', 'b'),
            (1, 'h', 'g'),
            (7, 'h', 'i'),
            (2, 'i', 'c'),
            (6, 'i', 'g'),
            (7, 'i', 'h')
        ])
    }
    
    return G


if __name__ == "__main__":
    G = generate_graph()
    kruskal(G)
