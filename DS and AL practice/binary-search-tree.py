


class Node:


    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree:


    def __init__(self):
        self.root = None
    

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        
        else:
            self.insert_node(data, self.root)

        

    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        
        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)

            else:
                node.rightChild = Node(data, node)

    def max(self):
        if self.root:
            return self.get_max(self.root)
    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)
        return node.data
        
    def remove_node(self, data, node):
        if node is None:
            return
        
        if data < node.data:
            return self.remove_node(data, node.leftChild)
        elif data > node.data:
            return self.remove_node(data, node.rightChild)
        else:
            if node.leftChild is None and node.rightChild is None:
                print("Remove a keaf node ... %d" % node.data)

                parent = node.parent
                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None
                if parent is None:
                    self.root = None
                del node


            elif node.leftChild is None and node.rightChild is not None:
                print("remove the node with right subtree")
                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                
                else:
                    self.root = node.rightChild
                
                node.rightChild.parent = parent
                del node
            

            elif node.leftChild is not None and node.rightChild is None:
                print("remove the node with left subtree")
                parent = node.parent


                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild

                    
                else:
                    self.root = node.leftChild
                
                node.leftChild.parent = parent
                del node

            
            else:
                print("remove with node with left and right both subtree")

                predecessor = self.get_predecessor(node.leftChild)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)
    
    def get_predecessor(self, node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)
        
        return node


    
    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)



         


    def min(self):
        if self.root:
            return self.get_min(self.root)
    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)
        return node.data

    def traversal(self):
        if self.root is not None:
            self.inOrderTraversal(self.root)

    def inOrderTraversal(self, node):
        if node.leftChild:
            self.inOrderTraversal(node.leftChild)

        print('%s' % node.data)
        if node.rightChild:
            self.inOrderTraversal(node.rightChild) 
class compare:
    
    def compare_tree(self, node1, node2):
        if not node1 or not node2:
            return node1 == node2
        if node1.data is not node2.data:
            return False
        
        return self.compare_tree(node1.leftChild, node2.leftChild) and self.compare_tree(node1.rightChild, node2.rightChild)


bst1 = BinarySearchTree()
bst2 = BinarySearchTree()

bst1.insert(120)
bst1.insert(20)
bst1.insert(30)
bst1.insert(2)
bst1.insert(200)
#print("the max value is:%d"  % bst.get_max(bst.root))
#print("the min valune is : %d" % bst.get_min(bst.root))
#bst.remove(20)


bst2.insert(120)
bst2.insert(20)
bst2.insert(30)
bst2.insert(2)
bst2.insert(200)

comp = compare()
print(comp.compare_tree(bst1.root, bst2.root))