#!/usr/bin/python

# BELLMAN-FORD ALGORITHM
# for single source shortest path

# works for negative edge weights as well
# returns false if a negative cycle is reachable 
# from the source

from pprint import pprint

# global variable
p = {}      # parent
d = {}      # distance(edge weight) from source

def relax(w, u, v):
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        p[v] = u

def initialize_single_source(G, s):
    global d
    global p

    for v in G['vertices']:
        d[v] = 99999
        p[v] = None
    d[s] = 0

def bellman_ford(G, s):
    global d

    initialize_single_source(G, s)

    for i in range(len(G['vertices']) - 1):
        for edge in G['edges']:
            w, u, v = edge
            relax(w, u, v)

    for edge in G['edges']:
        w, u, v = edge
        if d[v] > d[u] + w:
            return False
    
    pprint(d)
    pprint(p)
    return True 


if __name__ == "__main__":
    
    G = {
        'vertices' : ['s', 't', 'x', 'z', 'y'],
        'edges' : [
            (6, 's', 't'),
            (5, 't', 'x'),
            (-2, 'x', 't'),
            (7, 'z', 'x'),
            (9, 'y', 'z'),
            (7, 's', 'y'),
            (8, 't', 'y'),
            (2, 'z', 's'),
            (-3, 'y', 'x'),
            (-4, 't', 'z')
        ]
    }

    bellman_ford(G, 's')

