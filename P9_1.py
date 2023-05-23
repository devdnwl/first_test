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

def preorder(n):
    if n is not None:
        print(n.key, end=' ')
        preorder(n.left)
        preorder(n.right)
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.key, end=' ')
def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)
def count_leaf(n) :
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)
def calc_height(n) :
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1
    
class BSTNode:
    def __init__ (self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        
def search_value_bst(n, value):
    if n == None: return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)
    
#P9_1 ------------------
def search_max_bst_recur(n):
    if n.right == None:
        return n
    else:
        n = n.right
        return search_max_bst_recur(n)

def search_min_bst_recur(n):
    if n.left == None:
        return n
    else:
        n = n.left
        return search_min_bst_recur(n)
#-----------------------
def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)
    
def search_bst_iter(n, key):
    while n != None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False
    
def delete_bst_case1 (parent, node, root):
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root

def delete_bst_case2 (parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right
    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    return root

def delete_bst_case3 (parent, node, root):
    succp = node
    succ = node.right
    while (succ.left != None):
        succp = succ
        succ = succ.left
    if (succp.left == succ):
        succp.left = succ.right
    else:
        succp.right = succ.right
    node.key = succ.key
    node.value = succ.value
    node = succ;
    return root

def delete_bst(root, key):
    if root == None: return None
    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key: node = node.left
        else: node = node.right;
    if node == None: return None
    if node.left == None and node.right == None:
        root = delete_bst_case1 (parent, node, root)
    elif node.left == None or node.right == None:
        root = delete_bst_case2 (parent, node, root)
    else:
        root = delete_bst_case3 (parent, node, root)
    return root

class BSTMap():
    def __init__ (self):
        self.root = None
    def isEmpty (self): return self.root == None
    def clear(self): self.root = None
    def size(self): return count_node(self.root)
    def findMax(self): return search_max_bst_recur(self.root)
    def findMin(self): return search_min_bst_recur(self.root)
    def search(self, key): return search_bst(self.root, key)
    def searchValue(self, key): return search_value_bst(self.root, key)
    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)
    def delete(self, key):
        self.root = delete_bst(self.root, key)
    def display(self, msg = 'BTSMap :'):
        print(msg, end='')
        inorder(self.root)
        print()

def testBinarySearchTree() :
    print("\n======= 이진탐색트리 테스트 ===================================")
    map = BSTMap()
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    # 삽입 연산 테스트
    print("[삽입 연산] : ", data)
    for key in data:
        map.insert(key)
    map.display("[중위 순회] : ")
    print("최댓값= ", map.findMax().key)
    print("최소값= ", map.findMin().key)
    # 탐색 연산 테스트
    if map.search(26) != None : print('[탐색 26 ] : 성공')
    else : print('[탐색 26 ] : 실패')
    if map.search(25) != None : print('[탐색 25 ] : 성공')
    else : print('[탐색 25 ] : 실패')
    # 삭제 연산 테스트
    map.delete(3); map.display("[ 3 삭제] : ")
    map.delete(68); map.display("[ 68 삭제] : ")
    map.delete(18); map.display("[ 18 삭제] : ")
    map.delete(35); map.display("[ 35 삭제] : ")
testBinarySearchTree()