'''
[삽입 정렬 알고리즘]
- 정렬되지 않은 데이터에서 순서대로 데이터를 뽑아서 정렬된 데이터의 들어갈 위치를 검색하여 삽입하는 방식이다.
- 따라서, 데이터의 정렬된 정도에 따라 성능이 차이나게 된다.(최악의 경우 선택 정렬보다 성능이 떨어질 수 있다.)

- O 표기법에 의하면 O(N**2)의 실행시간을 갖는다.

- 삽입 정렬은 비교횟수가 적고 상대적으로 데이터의 이동 횟수가 많은 편에 속한다.
'''

import random
import time
import sys

compare_counter = 0
swap_counter = 0

def insertion_sort(random_list):
    global compare_counter, swap_counter
    # 리스트 첫 번째 값에 "-1"을 저장한다. 
    # 정렬할 데이터가 0보다 같거나 큰 양수값이기 때문에 최소값을 설정하기 위한 값이다.
    random_list.insert(0,-1)

    # s_idx 값을 기준으로 왼쪽으로 비교해 나간다.
    for s_idx in range(2, len(random_list)):
        # 현재 인덱스의 값을 temp에 저장한다.
        temp = random_list[s_idx]
        # 현재 인덱스는 ins_idx에 저장한다.(정렬되지 않은 데이터에서 최소값을 찾아서 넣을 위치)
        ins_idx = s_idx
        compare_counter += 1

        # (현재 인덱스 - 1)의 값이 temp보다 작은 값일 경우까지 반복한다.
        # temp가 정렬할 데이터 중 가장 작은 값이면 가장 처음 부분(0번 인덱스)까지 반복하게 된다.
        while random_list[ins_idx-1] > temp:
            swap_counter += 1
            # (현재 인덱스 - 1)의 값을 현재 인덱스 위치에 대입한다.
            # 값이 오른쪽으로 이동한다.
            random_list[ins_idx] = random_list[ins_idx-1]
            ins_idx = ins_idx - 1

        random_list[ins_idx] = temp
        print(random_list)

    del random_list[0]

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
    insertion_sort(num_list) # 선택 정렬 시작
    running_time = time.time() - start_time
    print("<정렬 후>")
    print(num_list)

    print(f"데이터의 크기 : {data}")
    print(f"비교 횟수 : {compare_counter}")
    print(f"교환 횟수 : {swap_counter}")
    print(f"실행 시간 : {running_time:.10}")