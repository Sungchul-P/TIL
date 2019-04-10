'''
[선택 정렬 알고리즘]
N개의 데이터를 갖는 선택 정렬 알고리즘은 2개의 반복문을 사용하여
(N * (N-1)/2)회의 비교를 한다.

N을 100이라고 하면, 비교 횟수는 (100*99/2) = 4950 회가 된다.
'''

import random
import time
import sys

compare_counter = 0
swap_counter = 0

def selected_sort(random_list):
    global compare_counter, swap_counter

    # 0 부터 (마지막 인덱스 - 1) 까지 반복 실행한다.
    for sel in range(len(random_list) - 1):
        # 현재 인덱스의 값을 최소값으로 가정한다.
        min = random_list[sel]
        minindex = sel

        # 현재 인덱스+1 부터 마지막 인덱스 까지 최소값을 찾는다.
        for step in range(sel+1, len(random_list)):
            compare_counter += 1
            # 기존에 설정된 최소값보다 작으면 변수의 값을 변경한다.
            if min > random_list[step]:
                min = random_list[step]
                minindex = step
                swap_counter += 1

        # 현재 인덱스의 값과 새롭게 찾은 최소값을 바꾼다(swap).
        random_list[minindex] = random_list[sel]
        random_list[sel] = min

if __name__ == '__main__':

    num_list = []
    data = 100

    # 매개변수 입력 값이 있으면 데이터의 크기를 변경한다.
    if len(sys.argv) >= 2:
        data = int(sys.argv[1])

    # 1 ~ 10 까지의 숫자를 중복되지 않게 무작위로 저장한다.
    '''
    while len(num_list) < data:
        new_number = random.randint(1,data)
        if new_number not in num_list:
            num_list.append(new_number)
    '''
    # 1 ~ 10 까지 숫자를 저장한 다음, 무작위로 섞는다.
    for i in range(1, data+1):
        num_list.append(i)

    random.shuffle(num_list)

    print("<정렬 전>")
    print(num_list)

    start_time = time.time()
    selected_sort(num_list) # 선택 정렬 시작
    running_time = time.time() - start_time
    print("<정렬 후>")
    print(num_list)

    print(f"데이터의 크기 : {data}")
    print(f"비교 횟수 : {compare_counter}")
    print(f"교환 횟수 : {swap_counter}")
    print(f"실행 시간 : {running_time:.7}")