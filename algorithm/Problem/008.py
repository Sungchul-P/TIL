# 008. 자연수 n이 소수인지 아닌지를 출력하기
# 소수(prime number) : 0보다 큰 자연수인 약수가 1과 자신뿐인 1보다 큰 자연수
# 예) 2, 3, 5, 7, 11, 13 ...

# 조건 01) 반복문을 사용하여 주어진 숫자 n을 2부터 n(for문) 또는 n-1(while문) 까지 반복하면서 나누고,
#           나눈 결과가 하나라도 나눈 몫을 구할 수 있으면 소수가 아닌 합성수이다.
# 조건 02) 위의 반복문이 끝난 결과로 제어 변수가 주어진 n과 같으면 소수이고 같지 않으면 합성수이다.

def solve(n):
    # i = 2
    # while i < n:
    #     if n % i == 0:
    #         break
    #     i += 1

    for i in range(2, n+1):
        if n % i == 0:
            break
    
    # print(i)
    if i == n:
        print("{}는 소수".format(n))
    else:
        print("{}는 합성수".format(n))

if __name__ == "__main__":
    solve(19)
    solve(130)
    solve(37)
    solve(20)
    solve(21)