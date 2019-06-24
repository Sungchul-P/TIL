# BST (Binary Search Tree)는 각 노드의 값이 해당 노드의 왼쪽 하위 트리에있는 모든 노드의 값보다 크고 
# 해당 노드의 오른쪽 하위 트리에있는 모든 노드의 값보다 작은 이진 트리입니다.

# 값이 포함되어 있는지 검색하는 함수 contains()
    # 효율적으로 로직을 구성하여 검색 시간을 최소화해야 한다.
# 반환 결과는 True, False

# 문제 원형 #
'''
import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    pass
        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))
'''

# 문제 풀이 #
import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):

    if root is None:
        return False
    elif value == root.value:
        return True
    elif value < root.value:
        return contains(root.left, value)
    else:
        return contains(root.right, value)

n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n6 = Node(value=6, left=None, right=None)
n5 = Node(value=5, left=None, right=n6)
n4 = Node(value=4, left=n3, right=n5)
n2 = Node(value=2, left=n1, right=n4)
        
print(contains(n2, 3))