# 007. 369 게임 만들기

# 조건 01) 3의 배수를 확인하는 코드를 작성해야 한다.
# 조건 02) 3의 배수가 아닌 경우는 숫자를 출력하고, 3의 배수인 경우는 "X"를 출력하는 코드를 작성해야 한다.
# 조건 03) 사용자로부터 입력 받은 n까지 위의 과정을 반복해야 한다.

def solve(n):
    for i in range(1, n+1):
        if i % 3 != 0:
            print(i, end=" ")
        else:
            print("X", end=" ")

if __name__ == "__main__":
    num = int(input("입력 : "))
    solve(num)