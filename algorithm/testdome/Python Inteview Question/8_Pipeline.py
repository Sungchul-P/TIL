# pipeline 메서드는 가변으로 함수를 받아 들여야하며 하나의 arg를 허용하는 helper 함수를 반환한다.
# 반환 된 함수는 매개 변수 arg를 사용하여 파이프 라인의 첫 번째 함수를 호출하고 
# 첫 번째 함수의 결과와 함께 두 번째 함수를 호출해야합니다.
# 반환 된 함수는 파이프 라인의 각 함수를 동일한 패턴에 따라 순서대로 계속 호출하고 마지막 함수에서 값을 반환해야합니다.

# 문제 원형 #
'''
def pipeline(*funcs):
    def helper(arg):
        pass
    return helper
            
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0
'''

# 문제 풀이 #
def pipeline(*funcs):
    def helper(arg):
        # 첫 번째 함수 호출 결과를 다시 다음 함수 인자 값으로 사용하고, 마지막 함수 호출 결과를 반환한다.
        for func in funcs:
            arg = func(arg)
        return arg
    return helper
            
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0