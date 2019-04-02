class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")
    node_A.next = node_B
    node_B.next = node_D
    node_B.prev = node_A
    node_D.next = node_E
    node_D.prev = node_B

def insert_node(data):
    global node_A
    # 인수로 받은 data로 새로운 노드를 생성한다.
    new_node = Node(data)
    # 새로운 노드를 삽입할 노드의 위치를 보관하기 위한 변수를 선언한다.
    node_P = node_A
    node_T = node_A
    # 삽입될 노드의 위치를 검색한다. (node_T)
    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next
    # 새로운 노드의 전후 노드에 next, prev 링크를 처리해 준다.
    new_node.next = node_T
    node_T.prev = new_node
    new_node.prev = node_P
    node_P.next = new_node

def delete_node(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next
    next_next_node = next_node.next

    if pre_node.data == del_data:
        nodeA = next_node
        del pre_node
        return

    while next_node:
        # 탐색이 완료되면 삭제할 노드는 next_node가 가리키게 된다.
        if next_node.data == del_data: # del_data == "D"
            next_next_node = next_node.next # "E"
            pre_node.next = next_node.next # "C".next = "E"
            next_next_node.prev = next_node.prev # "E".prev = "D".prev(즉, "C")
            del next_node # "D" 삭제
            # "A - B - C - E"
            break
        pre_node = next_node
        next_node = next_node.next

def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print()

if __name__ == "__main__":
    print("연결리스트 초기화 후")
    init_list()
    print_list()

    print("노드 C의 추가 후")
    insert_node("C")
    print_list()

    print("노드 D의 삭제 후")
    delete_node("D")
    print_list()