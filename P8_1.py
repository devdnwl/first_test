class TNode:
    def __init__ (self, elem, left, right):

def preorder(n):

def inorder(n):

def postorder(n):

def levelorder(root):

def count_node(n):

def count_leaf(n):

def calc_height(n):

class BinaryTree:
    def __init__ (self, root = None):
        self.root = root

    def isEmpty(self): return self.root == None
    def clear(self): self.root = None

    def printInOrder(self, msg='    In-Order : '):
        print(msg, end='')
        inorder(self.root)
        print('')
    def printPreOrder(self, msg='    Pre-Order : '):
        print(msg, end='')
        preorder(self.root)
        print('')
    def printPostOrder(self, msg='    Post-Order : '):
        print(msg, end='')
        postorder(self.root)
        print('')
    def printLevelOrder(self, msg='Level-Order : '):
        print(msg, end='')
        levelorder(self.root)
        print('')

def testP8_1_1():
    g = TNode('G', , )
    h = TNode('H', , )
    d = TNode('D', , )
    f = TNode('F', , )
    e = TNode('E', , )
    c = TNode('C', , )
    b = TNode('B', , )
    a = TNode('A', , )

    tree = BinaryTree()
    tree.printInOrder(' In-Order: ')
    tree.printPreOrder(' Pre-Order: ')
    tree.printPostOrder(' Post-Order: ')
    tree.printLevelOrder(' Level-Order: ')
    print(" 노드의 개수 = %d" % count_node(tree.root))
    print(" 단말의 개수 = %d" % count_leaf(tree.root))
    print(" 트리의 높이 = %d" % calc_height(tree.root))

def testP8_1_2():
    a = TNode('A', , )
    b = TNode('B', , )
    c = TNode('C', , )
    d = TNode('D', , )
    e = TNode('E', , )
    n1 = TNode('/', , )
    n2 = TNode('*', , )
    n3 = TNode('*', , )
    n4 = TNode('+', , )

    tree = BinaryTree( )
    tree.printInOrder (' In-Order : ')
    tree.printPreOrder (' Pre-Order : ')
    tree.printPostOrder (' Post-Order : ')
    tree.printLevelOrder('Level-Order : ')
    print(" 노드의 개수 = %d" % count_node(tree.root))
    print(" 단말의 개수 = %d" % count_leaf(tree.root))
    print(" 트리의 높이 = %d" % calc_height(tree.root))

print('P8.1 좌측 트리')
testP8_1_1()
print('P8.1 우측 트리')
testP8_1_2()