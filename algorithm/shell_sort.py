'''
[셸 정렬 알고리즘]
기본 구조는 삽입 정렬 알고리즘과 같지만 성능면에서는 훨씬 우수하다.
정렬할 데이터를 일정한 구간별로 쪼개서 그 구간 내에서 정렬한 후에 구간을 합쳐서 정렬 하기 때문이다.
(비교 횟수나 데이터의 이동 횟수가 훨씬 줄어들게 된다.)

h 값을 제어하는 것이 키포인트다. (3으로 나눈 값을 취한 경우..)
1) 0, 3, 6, 9 ... , 99 까지 정렬
2) 1, 4, 7, 10 ... 까지 정렬
3) h 를 3으로 나누어서 1이 될때까지 반복하면 대부분의 값이 정렬이 된 상태가 된다.
'''

import random
import time
import sys

def shell_sort(random_list):
    # 1 부터 MAX 값까지 변수 h를 3의 배수하여 1을 더한 값으로 증가시키면서
    # MAX 보다 큰 값이 될 때까지 반복한다.
    h = 1
    while h < len(random_list):
        h = h * 3 + 1
    
    # 데이터 크기가 100인 경우 h = 121
    h = h // 3 # 구간 분할을 위해 3으로 나누어 몫을 다시 저장한다.
    # 현재 h = 40
    
    while h > 0:
        for i in range(h):
            # start_index = 0 + 40
            start_index = i + h 

            # while 40 < 100
            while start_index < len(random_list):
                # temp = random_list[40]
                temp = random_list[start_index]
                insert_index = start_index

                # insert_index = 40
                # (40 > 40-1) and (random_list[40 - 40] > temp)
                while (insert_index > h-1) and (random_list[insert_index - h] > temp):
                    # random_list[40] = random_list[40 - 40]
                    random_list[insert_index] = random_list[insert_index - h]
                    # insert_index = 40 - 40
                    insert_index = insert_index - h

                # random_list[0] = temp
                # 즉, random_list[0] == random_list[40]
                random_list[insert_index] = temp
                # start_index = 40 + 40
                start_index = start_index + h

        h = h // 3

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
    shell_sort(num_list) # 셸 정렬 시작
    running_time = time.time() - start_time

    print("<정렬 후>")
    print(num_list)

    print(f"데이터의 크기 : {data}")
    print(f"실행 시간 : {running_time:.10}")