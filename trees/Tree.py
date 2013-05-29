class Tree:
    def __init__(self, value, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.value)

    def search_recursive(self, root, key):
        if root.value == key:
            print 'Key found'
            return root
        elif root.value > key:
            if root.left != None:
                return self.search_recursive(root.left, key)
            else:
                return False
        else: 
            if root.right != None:
                return self.search_recursive(root.right, key)
            else:
                return False

    def search_iterative(self, root, key):
        while root.value != key:
            if key < root.value:
                if root.left != None:
                    root = root.left
                else:
                    return False
            else:
                if root.right != None:
                    root = root.right
                else:
                    return False

        print 'Key found'
        return True

    def generate_test_tree(self):
        tree = Tree(50)

        keys = [73, 67, -75, 3, 14, -94, 100, 42, 78, 34, -2, -9, -7, -8, -6]
        for x in keys:
            tree.insert(tree, x)

        return tree

    def generate_rand_tree(self):
        import random

        tree = Tree(random.randint(-100, 100))
        #self.inorder_traversal(tree)

        for x in xrange(10):
            self.insert(tree, random.randint(-100, 100))

        self.inorder_traversal(tree)
        return tree

    def inorder_traversal(self, root):
        if root.left != None:
            self.inorder_traversal(root.left)

        print root.value, root.parent, root.left, root.right

        if root.right != None:
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        print root.value, root.parent, root.left, root.right

        if root.left != None:
            self.preorder_traversal(root.left)

        if root.right != None:
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root.left != None:
            self.postorder_traversal(root.left)

        if root.right != None:
            self.postorder_traversal(root.right)

        print root.value, root.parent, root.left, root.right

    def transplant(self, u, v):
        if u.parent == None:
            pass
            #return Tree(v)
        elif u.parent.left == u:
            u.parent.left = v
        elif u.parent.right == u:
            u.parent.right = v

        if u.parent != None and v != None:
            v.parent = u.parent
   
    def delete(self, root, key):
        while root.value != key:
            if key < root.value:
                if root.left != None:
                    root = root.left
                else:
                    return False
            else:
                if root.right != None:
                    root = root.right
                else:
                    return False

#       now the root points to the node to be deleted
        if root.left == None:
            self.transplant(root, root.right)
        elif root.right == None:
            self.transplant(root, root.left)
        else:
            y = self.successor(root)
            if y.parent != root:
                self.transplant(y, y.right)
                y.right = root.right
                y.right.parent = y

            self.transplant(root, y)
            y.left = root.left
            y.left.parent = y
            y.parent = root.parent

    def insert(self, root, key):
        if key < root.value:
            if root.left != None:
                self.insert(root.left, key)
            else:
                root.left = Tree(key)
                root.left.parent = root
        #elif key > root.value:
        # in case of duplicate keys, push them into
        # right subtree
        else:
            if root.right != None:
                self.insert(root.right, key)
            else:
                root.right = Tree(key)
                root.right.parent = root

    def minimum(self, node):
        while node.left != None:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != None:
            node = node.right
        return node

    def predecessor(self, node):
        if node.left != None:
            return node.left
        else:
            y = node.parent
            while y != None and y.right != node:
                node = y
                y = node.parent
            return node

    def successor(self, node):
        if node.right != None:
            return self.minimum(node.right)
        else:
            y = node.parent
            while y != None and y.left != node:
                node = y
                y = node.parent
            return node
