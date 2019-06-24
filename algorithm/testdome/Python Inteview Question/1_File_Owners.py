# Input : {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
# Output : {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}

# 문제 원형 #
'''
def group_by_owners(files):
    return None
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))
'''

# 문제 풀이 #
def group_by_owners(files):
    files_by_owner = {}
    for filename, owner in files.items():
        # dictionary에 키가 존재하지 않으면,
        # filename을 리스트를 값(value)으로 하여 저장한다.
        if owner not in files_by_owner:
            files_by_owner[owner] = [filename]
            
        # 키가 이미 존재하는 경우, 리스트 형식의 값(value)에 추가한다.
        else:
            files_by_owner.get(owner).append(filename)
    return files_by_owner
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))