# 목표 합계를 만들 수 있는 숫자의 조합을 리스트에서 찾아서 해당 인덱스를 단일 튜플로 반환한다.
# 해당되는 조합이 없는 경우 None을 반환한다.

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
# index_tuple(0, 3) as number = target_sum
# 0 and 3 (or 3 and 0) as 3 + 7 = 10
# 1 and 5 (or 5 and 1) as 1 + 9 = 10
# 2 and 4 (or 4 and 2) as 5 + 5 = 10
'''

# 문제 풀이 #
def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    return None

print(find_two_sum([3, 1, 5, 7, 5, 9], 10))