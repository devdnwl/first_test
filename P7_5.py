# BinaryMap
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return str("%s:%s"%(self.key, self.value))

class BinaryMap:
    def __init__(self):
        self.table = []
    def size(self):
        return len(self.table)
    def insert(self, key, value):
        self.table.append(Entry(key, value))
        i = self.size() - 1
        while i > 0 and self.table[i].key < self.table[i-1].key:
            self.table[i], self.table[i-1] = self.table[i-1], self.table[i]
            i -= 1
                
    def search(self, key):
        return binary_search(self.table, key, 0, self.size())
    
    def delete(self, key):
        for i in range(self.size()):
            if self.table[i].key == key:
                self.table.pop(i)
                return
            
    def display(self, msg):
        print(msg)
        for entry in self.table:
            print(" ", entry)
    
def binary_search(A, key, low, high):
    if (low <= high):
        middle = (low + high) // 2
        if key == A[middle].key:
            return A[middle]
        elif (key<A[middle].key):
            return binary_search(A, key, low, middle - 1)
        else:
            return binary_search(A, key, middle + 1, high)
    return None

# 테스트 코드
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