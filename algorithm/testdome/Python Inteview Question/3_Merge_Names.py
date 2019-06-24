# 이름이 저장된 두 리스트(Array)를 합친 결과를 리스트로 반환한다.
# 중복된 이름은 제거한다.

# 함수 호출 : unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])
# 결과 : ['Ava', 'Emma', 'Olivia', 'Sophia']

# 문제 원형 #
'''
def unique_names(names1, names2):
    return None

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
'''

# 문제 풀이 #
def unique_names(names1, names2):
    names = set(names1 + names2)
    return list(names)

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia