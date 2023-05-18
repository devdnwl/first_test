def preorder(n):

def inorder(n):

def postorder(n):

def levelorder(root):

def count_node(n):

def count_leaf(n) :

def calc_height(n) :

class BSTNode:
    def __init__ (self, key, value):

def search_bst(n, key):

def search_value_bst(n, value):

#P9_1 ------------------
def search_max_bst_recur(n):
def search_min_bst_recur(n):
#-----------------------
def search_bst(n, key):

def search_bst_iter(n, key):

def insert_bst(r, n):

def delete_bst_case1 (parent, node, root):

def delete_bst_case2 (parent, node, root):

def delete_bst_case3 (parent, node, root):

def delete_bst(root, key):

class BSTMap():
    def __init__ (self):

    def isEmpty (self): def clear(self):

    def size(self):

    def findMax(self):

    def findMin(self):

    def search(self, key):

    def searchValue(self, key):

    def insert(self, key, value=None):

    def delete(self, key):

    def display(self, msg = 'BTSMap :'):

def testBinarySearchTree() :
    print("\n======= 이진탐색트리 테스트 ===================================") 
    
    map = BSTMap()
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    
    # 삽입 연산 테스트
    print("[삽입 연산] : ", data)
    for key in data :
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