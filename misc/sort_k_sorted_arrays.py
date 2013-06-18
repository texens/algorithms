#!/usr/bin/python

# Question : Given input as k sorted arrays, generate a single sorted list as output.

import heapq 

def sort(arrays):
    q = []
    res = []
    index = {}

    for i in range(len(arrays)):
        heapq.heappush(q, (arrays[i][0], i, 0))
        index[i] = 0

    while q:
        u = heapq.heappop(q)
        print u
        array_num = u[1]
        index_num = u[2]

        res.append(u[0])
        if len(arrays[array_num]) > index[array_num] + 1:
            index[array_num] += 1
            heapq.heappush(q, (arrays[array_num][index[array_num]], array_num, index[array_num]))

    print res

arrays = [[1,12,23,34,45], [7, 9, 12, 15, 17], [2, 8, 12, 19, 20], [4]]
sort(arrays)
