# Prim's Algorithm

from pprint import pprint
import heapq

h = []
parent = {}

def v_in_h(h, v):
    for u in h:
        key, vertex = u
        if vertex == v:
            return True
    return False

def v_key(h, v):
    for u in h:
        key, vertex = u
        if vertex == v:
            return key
    return False

def decrease_key(h, v, key):
    for i in range(len(h)):
        old_key, vertex = h[i]
        if vertex == v:
            h[i] = (key, v)
    heapq.heapify(h)


def prim(G, r):
    global h
    global parent

    for vertex in G.keys():
        if vertex != r:
            heapq.heappush(h, (999, vertex))
            parent[vertex] = None

    heapq.heappush(h, (0, r))

    while len(h) > 0:
        u = heapq.heappop(h)
        key, vertex = u
        for v in G[vertex].keys():
            if v_in_h(h, v) and G[vertex][v] < v_key(h, v):
                decrease_key(h, v, G[vertex][v])
                parent[v] = vertex
    print "\nEdges that for the Minimum Spanning Tree : \n"
    pprint(parent)

def generate_graph():
    
    G = {
        'a' : {'b' : 4, 'h' : 8},
        'b' : {'a' : 4, 'c' : 8, 'h' : 11},
        'c' : {'b' : 8, 'd' : 7, 'f' : 4, 'i' : 2},
        'd' : {'c' : 7, 'e' : 9, 'f' : 14},
        'e' : {'d' : 9, 'f' : 10},
        'f' : {'c' : 4, 'd' : 14, 'e' : 10, 'g' : 2},
        'g' : {'h' : 1, 'i' : 6},
        'h' : {'a' : 8, 'b' : 11, 'g' : 1, 'i' : 7},
        'i' : {'c' : 2, 'g' : 6, 'h' : 7}
    }

    return G

if __name__ == "__main__":
    G = generate_graph()
    r = 'a'
    prim(G, 'a')
