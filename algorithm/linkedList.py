# 다음 노드를 가리키는 링크만이 존재한다.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 연결리스트를 초기화한다.
def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")
    node_A.next = node_B
    node_B.next = node_D
    node_D.next = node_E

# 삭제 알고리즘
'''
- 데이터의 이동 없이 링크를 끊어주고 삭제할 노드만을 해제해주면 된다.
- 삭제한 메모리를 해제한다.
'''
def delete_node(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next

    if pre_node.data == del_data:
        node_A = next_node
        del pre_node # 객체 삭제
        return

    # next_node에 노드가 존재하는 동안 반복한다.
    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node # 객체 삭제
            break
        pre_node = next_node
        next_node = next_node.next

# 삽입 알고리즘
'''
- 연결 리스트는 배열에 비해 시간의 효율성이 훨씬 높다.
- 연결 리스트는 동적으로 공간을 할당하여 사용할 수 있다.
- 포인터와 구조체로 되어 있기 때문에 배열의 인덱스에 비해서 이해하기 어렵다.
'''
def insert_node(data):
    global node_A
    # 인수로 받은 data로 새로운 노드를 생성한다.
    new_node = Node(data)
    # 새로운 노드를 삽입할 노드의 위치를 보관하기 위한 변수를 선언한다.
    node_P = node_A 
    node_T = node_A
    # 연결 리스트의 노드를 탐색한다.
        # node_T의 data가 작으면 다음 링크의 노드를 가리키도록 한다.
    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next

    # node_P -- [new_node] -- node_T 구조가 된다.
    new_node.next = node_T
    node_P.next = new_node

def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print()

if __name__ == "__main__":
    print("연결 리스트 초기화 후")
    init_list()
    print_list()
    print("노드 C를 추가한 후")
    insert_node("C")
    print_list()
    print("노드 D를 삭제한 후")
    delete_node("D")
    print_list()