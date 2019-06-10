# 005. 3과 5의 배수 계산하기

# 조건 01) 배수의 개념을 코드로 만들 수 있어야 한다.
# 조건 02) 3의 배수이면서 동시에 5의 배수인지를 확인하는 개념을 코드로 만들 수 있어야 한다.
# 조건 03) 반복문을 사용하여 1부터 n까지 1씩 증가하면서 제어 변수를 확인한다.

def check_multiple(n):
    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            print(i)

if __name__ == "__main__":
    check_multiple(100)