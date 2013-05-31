import Queue

class Color:
    WHITE = 0
    GRAY = 1
    BLACK = 2

class Vertex:
    def __init__(self, key = None, p = None, d = None, color = Color.WHITE):
        self.p = p
        self.d = d
        self.color = color
        self.key = key

Vertices = {}

def dfs(G, s):
    pass

def bfs(G, s):
    for adjl in G:
        for v in G[adjl]:
            v.p = None
            v.d = 0
            v.color = Color.WHITE

    s.color = Color.GRAY

    q = Queue.Queue()
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in G[u]:
            if v.color == Color.WHITE:
                v.color = Color.GRAY
                v.d = u.d + 1
                v.p = u
                q.put(v)

        u.color = Color.BLACK
        print u.key

def generate_test_graph():
    G_mat = {
            'A' : ['B', 'C', 'D'],
            'B' : ['E', 'F'],
            'C' : ['F'],
            'D' : ['B', 'F'],
            'E' : ['B', 'D', 'A'],
            'F' : ['B']
        }

    G = {}

    for u in G_mat:
        if u not in Vertices:
            Vertices[u] = Vertex(u)

        G[Vertices[u]] = []
        for v in G_mat[u]:
            if v not in Vertices:
                Vertices[v] = Vertex(v)
            G[Vertices[u]].append(Vertices[v]);

    return G
