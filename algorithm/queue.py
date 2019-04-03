# 리스트를 사용하여 쉽게 큐를 구현할 수 있다.
# 큐는 FIFO(First IN First Out) 방식이다.

# 데이터를 저장하는 함수
def put(item):
    queue.append(item)

# 데이터를 꺼내오는 함수
def get():
    return queue.pop(0) # 리스트의 첫 번째 값을 반환한다.

if __name__ == "__main__":
    queue = []
    put(1)
    put(2)
    put(3)
    put(4)
    print("현재 queue의 모습")
    print(queue)

    while queue:
        print("POP > {}".format(get()))