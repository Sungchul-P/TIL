# 목표 합계를 만들 수 있는 숫자의 조합을 리스트에서 찾아서 해당 인덱스를 단일 튜플로 반환한다.
# 해당되는 조합이 없는 경우 None을 반환한다.
# 모든 경우의 수를 찾는 것이 아니라 한 개의 쌍을 빠르게 찾아 반환하는 것이 목표다.

# Hint 01) 모든 경우의 수를 찾는 경우는 중첩 for문을 사용한다.
# Hint 02) 시간 복잡도를 줄이기 위해 딕셔너리 자료형을 활용한다.

# 문제 원형 #
'''
def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    return None

print(find_two_sum([3, 1, 5, 7, 5, 9], 10))

# [Output] #
# index_tuple(0, 3) as number = target_sum
# 0 and 3 (or 3 and 0) as 3 + 7 = 10
# 1 and 5 (or 5 and 1) as 1 + 9 = 10
# 2 and 4 (or 4 and 2) as 5 + 5 = 10
'''

# 문제 풀이 #

# 모든 조합을 찾아서 리스트로 반환(문제에서 요구하는 답은 아님)
'''
def find_two_sum(numbers, target_sum):
    result = list()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j]) == target_sum:
                result.append((i, j))
    return None if len(result) < 1 else result
'''
def find_two_sum(numbers, target_sum):
    find = {}
    
    for i, number in enumerate(numbers):
        
        try:
            # number가 키로 존재하는 경우 인덱스와 함께 튜플로 반환한다.
            # numbers 리스트의 3번 인덱스가 7 이므로 키가 이미 존재하여 (0, 3) 을 반환하게 된다.
            return (find[number], i)
        # 키가 없는 경우..
        except KeyError:
            # 숫자를 target_sum으로 뺀 값을 키(key)로 쓰고, 인덱스를 값(value)으로 저장한다.
            find[target_sum-number] = i
        
        # print(find)
        # {7: 0}
        # {7: 0, 9: 1}
        # {7: 0, 9: 1, 5: 2}

    return None

print(find_two_sum([3, 1, 5, 7, 5, 9], 10)) # (0, 3)