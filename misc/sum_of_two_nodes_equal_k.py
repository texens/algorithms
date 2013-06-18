#!/usr/bin/python

def func(arr, k):
    arr.sort()

    i = 0
    j = len(arr) - 1
    res = []

    while i < j:
        sum_ij = arr[i] + arr[j]
        if sum_ij == k:
            res.append((arr[i],arr[j]))
            i += 1
            j -= 1
        if sum_ij < k:
            i += 1
        elif sum_ij > k:
            j -= 1

    print res
    print len(res)


func([1, 2, 3, 4, 5, 7], 7)
