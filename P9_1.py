MAX_QSIZE = 5
class CircularQueue:        # 레벨 순회를 위한 원형큐
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
    
class BSTNode:                          # 이진탐색트리를 위한 노드 클래스
    def __init__ (self, key, value):    # 생성자: 키와 값을 받음
        self.key = key                  # 키(key)
        self.value = value              # 값(value)
        self.left = None                # 왼쪽 자식에 대한 링크
        self.right = None               # 오른쪽 자식에 대한 링크
        
def search_value_bst(n, value):                 # 이진탐색트리 탐색연산(preorder 사용) : 값을 이용한 탐색
    if n == None: return None                
    elif value == n.value:                      # n의 value와 동일->탐색성공
        return n
    res = search_value_bst(n.left, value)       # 왼쪽서브트리에서 탐색
    if res is not None:                         # 탐색이 성공이면
        return res                              # 결과 반환
    else:                                       # 왼쪽에서 탐색 실패이면
        return search_value_bst(n.right, value) # 오른쪽을 탐색해 결과 반환
    
#P9_1 ------------------
def search_max_bst_recur(n):
    if n.right == None:                 # 오른쪽 자식 값이 None이 되면
        return n                        # n 반환
    else:                               # None이 아니라면
        n = n.right                     # n에 오른쪽 자식 값을 넣고
        return search_max_bst_recur(n)  # 함수 순환

def search_min_bst_recur(n):
    if n.left == None:                  # 왼쪽 자식 값이 None이 되면
        return n                        # n 반환
    else:                               # None이 아니라면
        n = n.left                      # n에 왼쪽 자식 값을 넣고
        return search_min_bst_recur(n)  # 함수 순환
#-----------------------
def search_bst(n, key):                 # 이진탐색트리 탐색연산(순환 함수) 
    if n == None:
        return None
    elif key == n.key:                  # n의 키 값과 동일->탐색성공
        return n
    elif key < n.key:                   # key<n의 키
        return search_bst(n.left, key)  # 순환호출로 왼쪽 서브트리 탐색
    else:                               # key>n의 키
        return search_bst(n.right, key) # 순환호출로 오른쪽 서브트리 탐색
    
def search_bst_iter(n, key):    # 이진트리탐색 탐색연산(반복 함수)
    while n != None:            # n의 None이 아닐 때 까지
        if key == n.key:        # n의 키 값과 동일->탐색성공
            return n
        elif key < n.key:       # key<n의 키
            n = n.left          # n을 왼쪽 서브트리의 루트로 이동
        else:                   # key>n의 키
            n = n.right         # n을 오른쪽 서브트리의 루트로 이동
    return None                 # 찾는 키의 노드가 없음

def insert_bst(r, n):                       # 이진탐색트리 삽입연산 (노드를 삽입함): 순환구조 이용
    if n.key < r.key:                       # 삽입할 노드의 키가 루트보다 작으면
        if r.left is None:                  # 루트의 왼쪽 자식이 없으면
            r.left = n                      # n의 루트의 왼쪽 자식이 됨
            return True
        else:                               # 루트의 왼쪽 자식이 있으면
            return insert_bst(r.left, n)    # 왼쪽 자식에게 삽입하도록 함
    elif n.key > r.key:                     # 삽입할 노드의 키가 루트보다 크면
        if r.right is None:                 # 루트의 오른쪽 자식이 없으면
            r.right = n                     # n의 루트의 오른쪽 자식이 됨
            return True
        else:                               # 루트의 오른쪽 자식이 있으면
            return insert_bst(r.right, n)   # 오른쪽 자식에게 삽입하도록 함
    else:                                   # 키가 중독되면
        return False                        # 삽입하지 않음
    
def delete_bst_case1 (parent, node, root): 
    if parent is None:              # 삭제할 단말 노드가 루트이면
        root = None                 # 공백 트리가 됨
    else:
        if parent.left == node:     # 삭제할 노드가 부모의 왼쪽 자식이면
            parent.left = None      # 부모의 왼쪽 링크를 None
        else:                       # 오른쪽 자식이면
            parent.right = None     # 부모의 오른쪽 링크를 None
    return root                     # root가 변경될 수도 있으므로 변환

def delete_bst_case2 (parent, node, root):
    if node.left is not None:       # 삭제할 노드가 왼쪽 자식만 가짐
        child = node.left           # child는 왼쪽 자식
    else:                           # 삭제할 노드가 오른쪽 자식만 가짐
        child = node.right          # child는 오른쪽 자식
    if node == root:                # 없애려는 노드가 루트이면
        root = child                # 이제 child가 새로운 루트가 됨
    else:
        if node is parent.left:     # 삭제할 노드가 부모의 왼쪽 자식
            parent.left = child     # 부모의 왼쪽 링크를 변경
        else:                       # 삭제할 노드가 부모의 오른쪽 자식
            parent.right = child    # 부모의 오른쪽 링크를 변경
    return root                     # root가 변경될 수도 있으므로 변환

def delete_bst_case3 (parent, node, root):
    succp = node                    # 후계자의 부모 노드
    succ = node.right               # 후계자 노드
    while (succ.left != None):      # 후계자와 부모노드 탐색
        succp = succ
        succ = succ.left
    if (succp.left == succ):        # 후계자가 왼쪽 자식이면
        succp.left = succ.right     # 후계자의 오른쪽 지식 연결
    else:                           # 후계자가 오른쪽 자식이면
        succp.right = succ.right    # 후계자의 왼쪽 자식 연결
    node.key = succ.key             # 후계자의 키와 값을
    node.value = succ.value         # 삭제할 노드에 복사
    return root                     # 일관성을 위해 root 반환

def delete_bst(root, key):                              # 이진탐색트리 삭제연산 (노드를 삭제함)
    if root == None: return None                        # 공백 트리
    parent = None                                       # 삭제할 노드의 부모 탐색
    node = root                                         # 삭제할 노드 탐색
    while node != None and node.key != key:             # parent 탐색
        parent = node
        if key < node.key: node = node.left
        else: node = node.right;
    if node == None: return None                        # 삭제할 노드가 없음
    if node.left == None and node.right == None:        # case 1: 단말 노드
        root = delete_bst_case1 (parent, node, root)
    elif node.left == None or node.right == None:       # case 2: 유일한 자식
        root = delete_bst_case2 (parent, node, root)
    else:                                               # case 3: 두 개의 자식
        root = delete_bst_case3 (parent, node, root)
    return root                                         # 변경된 루트 노드를 반환

class BSTMap():             # 이진탐색트리를 이용한 맵
    def __init__ (self):    # 생성자
        self.root = None    # 트리의 루트 노드
    def isEmpty (self): return self.root == None    # 맵 공백 검사
    def clear(self): self.root = None               # 맵 초기화
    def size(self): return count_node(self.root)    # 레코드(노드) 수 계산
    def findMax(self): return search_max_bst_recur(self.root)
    def findMin(self): return search_min_bst_recur(self.root)
    def search(self, key): return search_bst(self.root, key)
    def searchValue(self, key): return search_value_bst(self.root, key)
    def insert(self, key, value=None):  # 삽입 연산
        n = BSTNode(key, value)         # 키와 값으로 새로운 노드 생성
        if self.isEmpty():              # 공백이면
            self.root = n               # 루트노드로 삽입
        else:                           # 공백이 아니면
            insert_bst(self.root, n)    # insert_bst() 호출
    def delete(self, key):                      # 삭제 연산
        self.root = delete_bst(self.root, key)  # delete_bst() 호출
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