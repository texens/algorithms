import bfs

G = bfs.generate_test_graph()

for key in G.keys():
    bfs.bfs(G, key)
    break
