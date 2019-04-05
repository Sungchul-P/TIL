# 트리 구조에서 사용할 노드에 대한 자료형을 만든다.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 노드를 생성하고 이진 트리의 형태를 갖도록 초기화한다.
def init_tree():
    global root

    new_node = Node("A")
    root = new_node
    new_node = Node("B")
    root.left = new_node
    new_node = Node("C")
    root.right = new_node
    new_node_1 = Node("D")
    new_node_2 = Node("E")
    node = root.left
    node.left = new_node_1
    node.right = new_node_2

    new_node_1 = Node("F")
    new_node_2 = Node("G")
    node = root.right
    node.left = new_node_1
    node.right = new_node_2

# 전위 순회(Pre-Order Traverse) 알고리즘
# 가운데 노드 - 왼쪽 노드 - 오른쪽 노드 순서로 방문
def preorder_traverse(node):
    if node == None: return # 트리의 끝이면 함수를 리턴

    print(node.data, end=' -> ')

    # 이진 트리 순회를 위해 재귀 호출을 사용한다.
    preorder_traverse(node.left)
    preorder_traverse(node.right)


# 중위 순회(In-Order Traverse) 알고리즘
# 왼쪽 자식 노드 - 부모 노드 - 오른쪽 자식 노드 순서로 방문
def inorder_traverse(node):
    if node == None: return
    
    inorder_traverse(node.left)
    print(node.data, end=' -> ')
    inorder_traverse(node.right)


# 후위 순회(Post-Order Traverse) 알고리즘
# 왼쪽 자식 노드 - 오른쪽 자식 노드 - 부모 노드 순서로 방문
def postorder_traverse(node):
    if node == None: return

    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data, end=' -> ')


# 단계 순회(Level-Order Traverse) 알고리즘
# 루트 노드부터 단계 순서대로 왼쪽 - 오른쪽 순서로 방문
# 큐를 사용해서 구현한다.
levelq = []

def levelorder_traverse(node):
    global levelq
    levelq.append(node)

    # 큐의 크기가 0이 아니라면 항목을 하나씩 가져와서 데이터를 출력한다.
    while len(levelq) != 0:
        # visit_node : 현재 노드
        visit_node = levelq.pop(0)
        print(visit_node.data, end=' -> ')

        # 왼쪽 또는 오른쪽 노드가 존재하면 큐에 추가한다.
        if visit_node.left != None:
            levelq.append(visit_node.left)
        if visit_node.right != None:
            levelq.append(visit_node.right)

# 프로그램 시작점
if __name__ == "__main__":
    init_tree()
    print("<전위 Preorder Traverse>")
    preorder_traverse(root)
    print()
    print("<중위 Inorder Traverse>")
    inorder_traverse(root)
    print()
    print("<후위 Postorder Traverse>")
    postorder_traverse(root)
    print()
    print("<단계 Levelorder Traverse>")
    levelorder_traverse(root)
    print()