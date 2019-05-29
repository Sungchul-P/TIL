# 003. 반복문을 사용하여 1부터 n까지 출력하기

# 조건01) 1부터 순서대로 화면에 출력해야 한다.
# 조건02) 출력하는 숫자가 n이 되면 프로그램을 종료한다.

def print_to_n(n):
    for i in range(1, n+1):
        print(i, end=" ")

if __name__ == "__main__":
    print_to_n(20)