from Tree import Tree

tree = Tree(1)
tree = tree.generate_test_tree()

tree.inorder_traversal(tree)
print 'Deleting the key'
tree.delete(tree, -75)

print 'Deleted the key'
tree.inorder_traversal(tree)

