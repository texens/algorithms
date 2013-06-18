#!/usr/bin/python

# Given pre-order traversal, reconstruct the binary search tree

class Node:
    def __init__(self, cargo):
        self.cargo = cargo
        self.left = None
        self.right = None

def make_tree(arr):
    if len(arr) == 1:
        node = Node(arr[0])
        return node

    if len(arr) == 0:
        return None

    for x in range(len(arr)):
        if arr[x] > arr[0]:
            break

    node = Node(arr[0])
    node.left = make_tree(arr[1:x])
    node.right = make_tree(arr[x:len(arr)])

    return node

arr = [12, 6, 2, -5, 8, 7, 29, 33, 30, 39]
tree = make_tree(arr)
