#!/usr/bin/python

# DIJKSTRA'S Algorithm
# Single Source Shortest Path for
# graph with non-negative weights

import heapq

from pprint import pprint

# global variable
h = []
path = []

def relax(w, u, v):
    global h
    global path

    for node in h:
        d, p, vertex = node
        if vertex == v:
            d_v = d

    for node in path:
        d, p, vertex = node
        if vertex == u:
            d_u = d
        elif vertex == v:
            d_v = d

    if d_v > d_u + w:
        d_v = d_u +w
        p_v = u
        for i in range(len(h)):
            _w, _p, _u = h[i]
            if _u == v:
                h[i] = (d_v, p_v, v)
                break

        heapq.heapify(h)

def dijkstra(G, s):
    global path
    global h
    h = G['vertices']
    heapq.heapify(h)

    while h:
        node = heapq.heappop(h)
        path.append(node)
        d, p, u = node

        for edge in G['edges']:
            w, vertex, v = edge
            if vertex == u:
                relax(w, u, v)

    print 'Edges in the single source shortest path : '
    for node in path:
        w, u, v = node
        print str(u) + '->' + str(v)
if __name__ == "__main__":
    G = {
        'vertices' : [
            (0, None, 's'), 
            (99999, None, 't'), 
            (99999, None, 'x'), 
            (99999, None, 'z'), 
            (99999, None, 'y')
        ],
        'edges' : [
            (10, 's', 't'),
            (1, 't', 'x'),
            (5, 's', 'y'),
            (2, 't' , 'y'),
            (3, 'y', 't'),
            (2, 'y', 'z'),
            (7, 'z', 's'),
            (9, 'y', 'x'),
            (4, 'x', 'z'),
            (6, 'z', 'x')
        ]
    }
    dijkstra(G, 's') 
