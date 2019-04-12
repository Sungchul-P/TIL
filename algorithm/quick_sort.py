'''
[퀵 정렬 알고리즘]
- 현존하는 정렬 알고리즘 중에서 가장 빠르다.
- 기준 데이터를 선택하고, 왼쪽/오른쪽으로 나눈 다음 각각 정렬해 나가는 방식이다.
    - 정렬 후에는, 양쪽에서 각 기준을 새로 선택한다.

"분할 정복 알고리즘(Divide and Conquer)"
    - 반복문을 하나만 사용하는 대신에 재귀 호출을 사용하여 데이터를 2개의 그룹으로 분할하여 정렬하는 방법

- O 표기법에 의하면 O(NlogN)
'''
import random
import time
import sys

# 두 값 교환
# x : 리스트
# i, j : 인덱스
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


# 주어진 데이터를 2개로 나누는 역할(중간값 반환)
def pivotFirst(x, lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark
    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[rmark] >= pivot_val:
            rmark -= 1

        if lmark <= rmark:
            swap(x, lmark, rmark)
            lmark += 1
            rmark -= 1

    swap(x, pivot_idx, rmark)
    return rmark


# 재귀 호출을 사용한다.
def quickSort(x, pivotMethod=pivotFirst):
    def _qsort(x, first, last):
        # 왼쪽 인덱스 first, 오른쪽 인덱스 last
        if first < last:
            # 중간값은 splitpoint에 저장한다.
            splitpoint = pivotMethod(x, first, last)
            _qsort(x, first, splitpoint-1) # 왼쪽 구간 정렬
            _qsort(x, splitpoint+1, last) # 오른쪽 구간 정렬
    _qsort(x, 0, len(x)-1)


if __name__ == '__main__':

    num_list = []
    data = 100

    # 매개변수 입력 값이 있으면 데이터의 크기를 변경한다.
    if len(sys.argv) >= 2:
        data = int(sys.argv[1])

    # 1 ~ 10 까지 숫자를 저장한 다음, 무작위로 섞는다.
    for i in range(1, data+1):
        num_list.append(i)

    random.shuffle(num_list)

    print("<정렬 전>")
    print(num_list)

    start_time = time.time()
    quickSort(num_list) # 퀵 정렬 시작
    running_time = time.time() - start_time
    print("<정렬 후>")
    print(num_list)