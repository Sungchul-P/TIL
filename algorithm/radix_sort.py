'''
[기수 정렬 알고리즘]
- 정렬할 데이터의 자릿수를 이용하여 데이터를 정렬하는 방법.
    - 예를 들어, 1의 자릿수 정렬 -> 10의 자릿수 정렬 -> ...

- O(D(N + Q))의 성능을 가진다.
    - D : 데이터 자릿수, N : 데이터 수, Q : 그에 해당하는 큐의 수
- 기수 정렬 알고리즘의 성능을 향상시키는 조건은 데이터의 수가 적거나 정렬할 데이터의 자릿수가 적은 경우다.
'''
import random
import time
import sys
from math import log10


def get_digit(number, base, pos):
    return (number // base ** pos) % base


def prefix_sum(array):
    for i in range(1, len(array)):
        array[i] = array[i] + array[i-1]
    return array


def radixsort(l, base=10):
    passes = int(log10(max(l)) + 1)
    output = [0] * len(l)

    for pos in range(passes):
        count = [0] * base

        for i in l:
            digit = get_digit(i, base, pos)
            count[digit] += 1

        count = prefix_sum(count)

        for i in reversed(l):
            digit = get_digit(i, base, pos)
            count[digit] -= 1
            new_pos = count[digit]
            output[new_pos] = i

        l = list(output)
    return output


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
    sorted_list = radixsort(num_list) # 기수 정렬 시작
    running_time = time.time() - start_time
    print("<정렬 후>")
    print(sorted_list)