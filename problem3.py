class Node(object):

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.target_node = None

    def insert(self, data):

        self.root = Node(data[0])

        self.root.leftChild = Node(data[1])
        self.root.leftChild.parent = self.root
        self.root.rightChild = Node(data[2])
        self.root.rightChild.parent = self.root

        self.root.leftChild.leftChild = Node(data[3])
        self.root.leftChild.leftChild.parent = self.root.leftChild
        self.root.leftChild.rightChild = Node(data[4])
        self.root.leftChild.rightChild.parent = self.root.leftChild

        self.root.rightChild.leftChild = Node(data[5])
        self.root.rightChild.leftChild.parent = self.root.rightChild
        self.root.rightChild.rightChild = Node(data[6])
        self.root.rightChild.rightChild.parent = self.root.rightChild

        self.root.leftChild.leftChild.leftChild = Node(data[7])
        self.root.leftChild.leftChild.leftChild.parent = self.root.leftChild.leftChild
        self.root.leftChild.leftChild.rightChild = Node(data[8])
        self.root.leftChild.leftChild.rightChild.parent = self.root.leftChild.leftChild

    def traverse(self, data):
        if self.root:
            self.traverseInOrder(self.root, data)
        return self.target_node

    # O(N)
    def traverseInOrder(self, node, data):

        if node.leftChild:
            self.traverseInOrder(node.leftChild, data)

        if data == node.data:
            self.target_node = node

        if node.rightChild:
            self.traverseInOrder(node.rightChild, data)


nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bst = BinarySearchTree()
bst.insert(nodes)


def lca(node1, node2):
    list1 = []
    node = bst.traverse(node1)
    while node.parent != None:
        list1.append(node.data)
        node = node.parent
    list1.append(node.data)

    list2 = []
    node = bst.traverse(node2)
    while node.parent != None:
        list2.append(node.data)
        node = node.parent
    list2.append(node.data)

    list1 = set(list1)
    a = list(list1.intersection(list2))[-1]
    print(a)


lca(5, 7)
