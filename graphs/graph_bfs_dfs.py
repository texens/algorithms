import Queue

class Color:
    WHITE = 0
    GRAY = 1
    BLACK = 2

class Vertex:
    def __init__(self, key = None, p = None, d = None, color = Color.WHITE, f = None):
        self.p = p
        self.d = d
        self.f = f
        self.color = color
        self.key = key

Vertices = {}
t = 0

def dfs(G):
    for u in Vertices:
        v = get_vertex(u)
        if v.color == Color.WHITE:
            dfs_visit(G, v)

def dfs_visit(G, u):
    global t
    t = t + 1
    u.d = t
    u.color = Color.GRAY

    for v in G[u]:
        if v.color == Color.WHITE:
            v.p = u
            dfs_visit(G, v)

    t = t + 1
    u.f = t
    u.color = Color.BLACK

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
        #print u.key

def print_path(G, s, v):
    if v == s:
        print s.key
    elif v.p == None:
        print 'None path exists from s to v'
    else:
        print v.key
        print_path(G, s, v.p)

def get_vertex(key):
    return Vertices[key]

def print_vertex(key):
    v = get_vertex(key)
    if v:
        if v.p:
            p = str(v.p.key)
        else:
            p = 'None'
        print 'key = ' + str(v.key) + ', parent = ' + p + ', d = ' + str(v.d) + ', f = ' + str(v.f)
    else:
        print 'None'

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
