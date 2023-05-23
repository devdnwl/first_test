# BinaryMap
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self): 
        return str("%s:%s"%(self.key, self.value))  # 엔트리 객체를 문자열로 변환

class BinaryMap:            # 이진탐색 맵
    def __init__(self):
        self.table = []     # 맵의 레코드 테이블

    def size(self): return len(self.table)  # 레코드의 개수

    def insert(self, key, value):
        self.table.append(Entry(key, value))    # 레코드에 엔트리 추가
        i = self.size() - 1                     # i: 레코드의 최대 인덱스 값
        while i > 0 and self.table[i].key < self.table[i-1].key:            # i가 0보다 크고, i번째 key가 i-1번째 key보다 작을 때 반복 (=정렬이 완전히 될 때까지)
            self.table[i], self.table[i-1] = self.table[i-1], self.table[i] # 레코드를 앞 뒤로 교환함
            i -= 1      # i를 1씩 줄임
                
    def search(self, key):  # 이진 탐색 함수에 레코드와 key와 최소, 최대(레코드의 길이)를 넣어 탐색
        return binary_search(self.table, key, 0, self.size())
    
    def delete(self, key):                  
        for i in range(self.size()):        
            if self.table[i].key == key:    # 삭제할 위치를 먼저 찾고
                self.table.pop(i)           # 리스트의 pop으로 삭제
                return
            
    def display(self, msg): # 보기 좋게 출력
        print(msg)
        for entry in self.table:    # 테이블의 모든 엔트리에 대해
            print(" ", entry)       # 출력(연산자 중복함수 사용)
    
def binary_search(A, key, low, high):
    if (low <= high):                   # 항목들이 남아 있으면(종료 조건)
        middle = (low + high) // 2      # 정수 나눗셈 //에 주의할 것
        if key == A[middle].key:        # 탐색 성공
            return A[middle]            
        elif (key<A[middle].key):       # 왼쪽 부분리스트 탐색
            return binary_search(A, key, low, middle - 1)
        else:                           # 오른쪽 부분리스트 탐색
            return binary_search(A, key, middle + 1, high)
    return None                         # 탐색 실패

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