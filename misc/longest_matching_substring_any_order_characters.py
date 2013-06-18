#!/usr/bin/python

# Question :
# I could not find an answer to the following hypothetical interview question:
# Given two string sequences of length N, how can you find the maximum length of matching substrings irrespective of order.
# For example, given seq1 = "ABCDEFG", and seq2 = "DBCAPFG", the maximum length window is 4. (ABCD from seq1 and DBCA from seq2).

# http://stackoverflow.com/questions/16999402/longest-matching-substring-irrespective-of-the-order-of-characters/17003022?noredirect=1#comment24595409_17003022


def find_windows(a, b):
    max_w = min(len(a), len(b)) 

    for w in reversed(range(max_w)):
        for i in range(len(a) - w):
            for j in range(len(b) - w):
                if check_anagram(a[i:i + w], b[j:j + w]) == 1:
                    print 'window size = ' + str(w)
                    print a[i:i + w], b[j:j + w] 
                    return

def check_anagram(p, q):
    d = {}
    for x in p:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for x in q:
        if x in d:
            d[x] -= 1
        else:
            d[x] = -1

    l = [x for x in d if d[x] != 0]
    if len(l) == 0:
        return 1
    else:
        return 0

find_windows("XABCDEFGYZ", "YZDBACPFGX")                    
