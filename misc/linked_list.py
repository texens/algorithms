class Node:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, cargo):
        new_node = Node(cargo)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_node(self, index):
        node = self.head
        for x in range(index - 1):
            prev = node.next
        prev.next = prev.next.next

    def print_list(self):
        node = self.head
        while node != None:
            print node.cargo
            node = node.next

ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)
ll.add_node(6)
ll.add_node(7)
ll.remove_node(3)
ll.add_node(8)
ll.add_node(9)
ll.add_node(10)
ll.add_node(11)
ll.add_node(12)
ll.add_node(13)
ll.add_node(14)

ll.print_list()
