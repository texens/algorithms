#!/usr/bin/python
# Longest Common Subsequence

# Note that Python has a call by object funda
# Names are tabs associated to objects
# When you reassign an integer, you actually
# destroy the old tag and create a new tag
# and assign it to this new rassigned integer
# Every object has a id, a type and content
# Usually, id and type can't be changed for
# an object. You can see the id and type of an 
# object by using id(object) and type(object)

# In case of lists, the list object is passed
# as a whole. If you edit the list anywhere in 
# any function, then it will change for the
# entire program. Hence, use a copy in such scenarios

# Some useful links : 
# http://stackoverflow.com/questions/845110/emulating-pass-by-value-behaviour-in-python

def lcs(a, b, common1):
    common = get_copy(common1)
    if len(a) == 0 or len(b) == 0:
        return 0, common
    elif a[len(a) - 1] == b[len(b) - 1]:
        common.append(a[len(a) - 1])
        res = lcs(a[:len(a) - 1], b[:len(b) - 1], common)
        return 1 + res[0], res[1] 
    else:
        res1 = lcs(a[:len(a) - 1], b, common)
        common = get_copy(common1)
        res2 = lcs(a, b[:len(b) - 1], common)

        if res1[0] > res2[0]:
            return res1
        else:
            return res2

def main():
    a = "abcdef"
    b = "adf"

    common = []
    res = lcs(a, b, common)
    res[1].reverse()
    print res[0]
    print res[1]

def get_copy(l):
    L = []
    for i in l:
        L.append(i)
    return L

main()
