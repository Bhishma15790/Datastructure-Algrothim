


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class double_linked(Node):

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
    

    def tarvesal_forward(self):
        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next

    def tarvesal_backward(self):
        actual_node = self.tail

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.previous


if __name__ == '__main__': 
    linkedlist = double_linked()
    linkedlist.insert(1)
    linkedlist.insert(2)
    linkedlist.insert(3)
    linkedlist.insert(4)
    linkedlist.tarvesal_forward()




