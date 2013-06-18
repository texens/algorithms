#!/usr/bin/python

#You are given a set of links, e.g.
#
#a ---> b
#b ---> c
#b ---> d
#a ---> e 
#
#Print the tree that would form when each pair of these links that has the same character as start and end point is joined together. You have to maintain fidelity w.r.t. the height of nodes, i.e. nodes at height n from root should be printed at same row or column. For set of links given above, tree printed should be 
#
#-->a
#   |-->b
#   |   |-->c
#   |   |-->d
#   |-->e
#Note that these links need not form a single tree; they could form, ahem, a forest. Consider the following links
#
#a ---> b
#a ---> g
#b ---> c
#c ---> d
#d ---> e
#c ---> f
#z ---> y
#y ---> x
#x ---> w
#
#The output would be following forest.
#
#-->a
#   |-->b
#   |   |-->c
#   |   |   |-->d
#   |   |   |   |-->e
#   |   |   |-->f
#   |-->g
#
#-->z
#   |-->y
#   |   |-->x
#   |   |   |-->w
#
#You can assume that given links can form a tree or forest of trees only, and there are no duplicates among links.


d = []
d.append(('a', 'b'))
d.append(('b', 'c'))
d.append(('b', 'd'))
d.append(('a', 'e'))

res = {}
gmax = 0

for x in range(len(d)):
    a, b = d[x]
    gmax += 1
    if a in res.keys():
        res[b] = (res[a][0] + 1, gmax)
    else:
        res[a] = (0, gmax)
        gmax += 1
        res[b] = (1, gmax)

print res
