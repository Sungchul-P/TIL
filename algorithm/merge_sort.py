'''
[병합 정렬 알고리즘]
- 이미 정렬되어 있는 데이터들을 하나로 합쳐서 정렬하는 방법이다.
- 파일에 정렬되어 있는 데이터들을 하나로 합쳐서 정렬하는 경우에도 종종 사용된다.
'''

#!/usr/bin/python
from math import log10
from random import randint
import sys

# 최소한의 데이터를 갖는 런이 될 때까지 재귀 호출이 된다.
def merge_sort(mylist):
    if len(mylist) <= 1: return mylist
    half = len(mylist) // 2 # 중간 값

    left_list = merge_sort(mylist[:half]) # 각 런의 가장 왼쪽 데이터
    right_list = merge_sort(mylist[half:]) # 오른쪽 데이터
    merged_list = []

    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] > right_list[0]:
            merged_list.append(right_list[0])
            right_list.pop(0)
        else:
            merged_list.append(left_list[0])
            left_list.pop(0)
    if len(left_list) > 0: merged_list += left_list
    if len(right_list) > 0: merged_list += right_list
    return merged_list

if __name__ == '__main__':

    data = 100

    # 매개변수 입력 값이 있으면 데이터의 크기를 변경한다.
    if len(sys.argv) >= 2:
        data = int(sys.argv[1])

    # 1 ~ 99999 의 숫자를 data 개수 만큼 리스트로 저장한다.
    num_list = [random.randint(1,99999) for x in range(data)]

    print("<정렬 전>")
    print(num_list)

    start_time = time.time()
    sorted_list = merge_sort(num_list) # 병합 정렬 시작
    running_time = time.time() - start_time
    print("<정렬 후>")
    print(sorted_list)