# https://www.testdome.com/d/python-interview-questions/9

# 파일 시스템의 cd 명령을 클래스로 구현한다.

# 조건
# Root path is '/'.
# Path separator is '/'.
# Parent directory is addressable as '..'.
# Directory names consist only of English alphabet letters (A-Z and a-z).
# The function should support both relative and absolute paths.
# The function will not be passed any invalid paths.
# Do not use built-in path-related functions.

# 문제 원형 #
'''
class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        pass

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
'''

# 문제 풀이 #
class Path:
    def __init__(self, path):
        self.current_path = path

    # Passes 3/4 tests
    def cd(self, new_path):
        # 상대 경로(상위로 이동)
        if new_path.startswith('..'):
            current = self.current_path.split('/') # ['', 'a', 'b', 'c', 'd']
            new_path = new_path.split('/') # ['..', 'x']

            for directory in new_path:
                if directory == '..':
                    current.pop() # '..'이 있으면 상위로 이동하기 위해 current의 마지막 요소를 제거
                else:
                    current.append(directory) # 디렉토리 이름이면 current에 추가

            self.current_path = '/'.join(current)

        # 절대 경로
        elif new_path.startswith('/'):
            # new_path = '/x/y/../z'
            if new_path.__contains__('..'):
                new_path = new_path.split('/') # ['', x', 'y', '..', 'z']
                # print(new_path)
                for idx, directory in enumerate(new_path):
                    if directory == '..':
                        new_path.pop(idx)
                        new_path.pop(idx-1) # '..' 이 발견되면 자신 인덱스와 직전 인덱스 요소를 제거

                self.current_path = '/'.join(new_path)
            else:
                self.current_path = new_path
                
        # 상대 경로(하위로 이동)
        else:
            child_path = self.current_path.split('/')
            child_path.append(new_path)
            self.current_path = "/".join(child_path)

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path) # '/a/b/c/x'.
path.cd('../x/y/../z')
print(path.current_path) # '/a/b/c/x/y/z'.
path.cd('/x/y/../z')
print(path.current_path) # '/a/b/c/x/y/z'.

# 다른 사람 풀이도 참고해 보자.
# https://github.com/ShawnROGrady/TestdomePython/blob/master/Path.py
'''
def cd(self, new_path):
    i=0
    new_pathList=new_path.split('/')
    pathLength=len(new_pathList)
    pathList=self.current_path.split('/')
    #print(new_PathList)
    if new_pathList[0]=='':
        #direct pathname
        del pathList[:]
        pathList.append('/'+new_pathList[1])
        i=i+2
    while(i<pathLength):
        j=len(pathList)-1
        if new_pathList[i]=='..':
            #parent directory
            pathList.pop(j)
        else:
            pathList.append(new_pathList[i])
        i=i+1
    self.current_path="/".join(pathList)

    pass
'''
