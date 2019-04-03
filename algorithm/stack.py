# 리스트를 사용하여 쉽게 스택을 구현할 수 있다.
# 스택은 LIFO(Last IN First Out) 방식이다.

# 데이터를 저장하는 함수
def push(item):
    stack.append(item)

# 데이터를 꺼내오는 함수
def pop():
    return stack.pop() # 리스트의 마지막 값을 반환한다.

if __name__ == "__main__":
    stack = []
    push(1)
    push(2)
    push(3)
    push(4)
    print("현재 stack의 모습")
    print(stack)

    while stack:
        print("POP > {}".format(pop()))