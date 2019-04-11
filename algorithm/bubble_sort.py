'''
[버블 정렬 알고리즘]
순차적으로 바로 옆에 있는 데이터와 비교해서 옆의 데이터가 크면 위치를 변경한다.
최선의 경우(모두 정렬된 경우) : 이동 횟수 0, 비교 횟수 (N*N)/2
최악의 경우 : 이동 횟수, 비교 횟수 모두 (N*N)/2

O 표기법에 의하면 O(N**2) 의 실행시간을 갖는다. (비효율적인 알고리즘)
'''

import random
import time
import sys

compare_counter = 0
swap_counter = 0

def bubble_sort(random_list):
    global compare_counter, swap_counter

    for start_index in range(len(random_list) - 1):
        # 가장 마지막 위치에서부터 한 칸씩 줄어들면서 반복 실행하게 된다.
        for index in range(1, len(random_list) - start_index):
            compare_counter += 1
            # 이전 값이 지금 값보다 크면 교환 한다.(가장 큰 값이 마지막 위치로 이동된다.)
            if random_list[index - 1] > random_list[index]:
                temp = random_list[index - 1]
                random_list[index - 1] = random_list[index]
                random_list[index] = temp
                swap_counter += 1


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
    bubble_sort(num_list) # 버블 정렬 시작
    running_time = time.time() - start_time
    print("<정렬 후>")
    print(num_list)

    print(f"데이터의 크기 : {data}")
    print(f"비교 횟수 : {compare_counter}")
    print(f"교환 횟수 : {swap_counter}")
    print(f"실행 시간 : {running_time:.7}")