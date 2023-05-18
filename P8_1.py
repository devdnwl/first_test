MAX_QSIZE = 5
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE
    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1)%MAX_QSIZE
    def clear(self): self.front = self.rear
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]
    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

class TNode:
    def __init__ (self, elem, left, right):
        self.elem = elem
        self.left = left
        self.right = right

def preorder(n):
    if n is not None:
        print(n.elem, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.elem, end=' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.elem, end=' ')

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.elem, end=' ')
            if n.left is not None:
                queue.enqueue(n.left)
            if n.right is not None:
                queue.enqueue(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)
    
def count_leaf(n):
    if n is None:
        return 0 
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if(hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1
    
class BinaryTree:
    def __init__ (self, root = None):
        self.root = root

    def isEmpty(self): return self.root == None
    def clear(self): self.root = None

    def printInOrder(self, msg='In-Order : '):
        print(msg, end='')
        inorder(self.root)
        print('')
    def printPreOrder(self, msg='Pre-Order : '):
        print(msg, end='')
        preorder(self.root)
        print('')
    def printPostOrder(self, msg='Post-Order : '):
        print(msg, end='')
        postorder(self.root)
        print('')
    def printLevelOrder(self, msg='Level-Order : '):
        print(msg, end='')
        levelorder(self.root)
        print('')

def testP8_1_1():
    g = TNode('G', None, None)
    h = TNode('H', None, None)
    d = TNode('D', None, None)
    f = TNode('F', None, None)
    e = TNode('E', g, h)
    c = TNode('C', e, f)
    b = TNode('B', d, None)
    a = TNode('A', b, c)

    tree = BinaryTree(a)
    tree.printInOrder('   In-Order: ')
    tree.printPreOrder('  Pre-Order: ')
    tree.printPostOrder(' Post-Order: ')
    tree.printLevelOrder('Level-Order: ')
    print(" 노드의 개수 = %d" % count_node(tree.root))
    print(" 단말의 개수 = %d" % count_leaf(tree.root))
    print(" 트리의 높이 = %d" % calc_height(tree.root))

def testP8_1_2():
    a = TNode('A', None, None)
    b = TNode('B', None, None)
    c = TNode('C', None, None)
    d = TNode('D', None, None)
    e = TNode('E', None, None)
    n1 = TNode('/', a, b)
    n2 = TNode('*', n1, c)
    n3 = TNode('*', n2, d)
    n4 = TNode('+', n3, e)

    tree = BinaryTree(n4)
    tree.printInOrder ('   In-Order : ')
    tree.printPreOrder ('  Pre-Order : ')
    tree.printPostOrder (' Post-Order : ')
    tree.printLevelOrder('Level-Order : ')
    print(" 노드의 개수 = %d" % count_node(tree.root))
    print(" 단말의 개수 = %d" % count_leaf(tree.root))
    print(" 트리의 높이 = %d" % calc_height(tree.root))

print('P8.1 좌측 트리')
testP8_1_1()
print('P8.1 우측 트리')
testP8_1_2()