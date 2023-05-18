class Entry:
    def __init__(self, key, value):
    def __str__(self):

class BinaryMap:
    def __init__(self):
    
    def size(self):
    
    def insert(self, key, value):
    
    def search(self, key):
    
    def delete(self, key):

    def display(self, msg):
    
def binary_search(A, key, low, high:

map = BinaryMap()

map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequential search', '선형 탐색')
map.insert('game', '게임')
map.insert('binary search', '이진 탐색')
map.display("나의 단어장: ")

print("탐색:game --> ", map.search('game'))
print("탐색:over --> ", map.search('over'))
print("탐색:data --> ", map.search('data'))

map.delete('game')
map.display("나의 단어장: ")