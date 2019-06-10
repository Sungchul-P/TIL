# 009. 2 ~ N 사이의 모든 소수를 추출하기

# 조건 01) 2부터 N 까지의 반복문으로 소수 확인 함수를 호출한다.

def check_prime(n):
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
    n = 20
    for i in range(2, n+1):
        check_prime(i)