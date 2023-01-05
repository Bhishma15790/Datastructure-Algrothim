


class node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class linkedlist:
    
    def __init__(self):
        self.headnode = None
        self.noofNode = 0
   # linear time complexity o(1) 
    def add_linkedlist(self, data):
        self.noofNode = self.noofNode + 1
        new_node = node(data)

        if not self.headnode:
            self.headnode = new_node
        else:
            new_node.nextNode = self.headnode
            self.headnode = new_node
    def reverse_linkedlist(self):
        current_node = self.headnode
        nextNode = None
        previousNode = None

        while current_node is not None:
            nextNode = current_node.nextNode
            current_node.nextNode = previousNode
            previousNode = current_node
            current_node = nextNode
        self.headnode = previousNode


    def middle_node(self):
        fast_ponter = self.headnode
        slow_ponter = self.headnode

        while fast_ponter.nextNode and fast_ponter.nextNode.nextNode:
            fast_ponter = fast_ponter.nextNode.nextNode
            slow_ponter = slow_ponter.nextNode
        return slow_ponter

# o(1)
    def add_end(self, data):
        self.noofNode = self.noofNode + 1
        new_node = node(data)
        
        actual_node = self.headnode

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode
            actual_node.nextNode = new_node

    def remove(self, data):
        if self.headnode is None:
            return
        actual_node = self.headnode
        previous_node = None
        
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode
        
        if actual_node is None:
            return
        
        self.noofNode = self.noofNode-1

        if previous_node is  None:
            self.headnode =  actual_node.nextNode
        else:
            previous_node.nextNode = actual_node.nextNode





# o(1)
    def size_of_linkedlist(self):
        return self.noofNode
    

# o(N)
    def traversal(self):

        actual_node = self.headnode

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode
linked = linkedlist()

linked.add_linkedlist(4)
linked.add_linkedlist(43)
linked.add_linkedlist(41)
linked.add_linkedlist(5)
linked.traversal()
# linked.remove(43)

# print(linked.middle_node().data)
linked.reverse_linkedlist()
linked.traversal()
