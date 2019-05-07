'''
[힙 정렬 알고리즘]
- 우선순위 큐(Priority Queue)를 이용하여 우선순위에 따라 정렬을 하는 알고리즘.
- 우선순위 큐는 가장 앞쪽에 있는 데이터가 가장 큰 값을 갖는 데이터가 되어야 한다.
- 힙 정렬 알고리즘은 트리 구조로 구성되며 루트 노드가 가장 큰 값을 갖게 된다.
- 운영체제나 네트워크와 같은 시스템 레벨에서 자주 사용되는 알고리즘이다.
'''

#!/usr/bin/python
from math import log10
from random import randint
import sys

def left_node(idx=None):
    return ((idx + 1) << 1) - 1

def right_node(idx=None):
    return (idx + 1) << 1

def up_heap(mylist=None, idx=None, heap_size=None):
    l_node = left_node(idx)
    r_node = right_node(idx)

    if l_node <= heap_size and mylist[l_node] > mylist[idx]:
        largest = l_node
    else:
        largest = idx

    if r_node <= heap_size and mylist[r_node] > mylist[largest]:
        largest = r_node

    if largest != idx:
        mylist[idx], mylist[largest] = mylist[largest], mylist[idx]
        up_heap(mylist, largest, heap_size)

def build_heap(mylist=None):
    heap_size = len(mylist) - 1
    for i in reversed(range(len(mylist) // 2)):
        up_heap(mylist, i, heap_size)

def heap_sort(heap=None):
    tmp_array = list()
    for i in range(len(heap)):
        tmp_array.append(heap.pop(0))
        up_heap(heap, 0, len(heap) - 1)
    return tmp_array

if __name__ == '__main__':

    data = 100

    # 매개변수 입력 값이 있으면 데이터의 크기를 변경한다.
    if len(sys.argv) >= 2:
        data = int(sys.argv[1])

    # 1 ~ 99999 의 숫자를 data 개수 만큼 리스트로 저장한다.
    num_list = [randint(1,99999) for x in range(data)]

    print("<정렬 전>")
    print(num_list)

    build_heap(num_list)

    sorted_list = heap_sort(num_list)

    print("<정렬 후>")
    print(sorted_list)