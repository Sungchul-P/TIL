# 015. 소인수분해 구하기

# 소인수분해 : 소수가 아닌 합성수를 소수의 곱으로 나타내는 방법

# 조건01) 주어진 숫자 n이 i로 나누어지면 해당 i는 n의 인수에 해당하며 n = n // i 로 저장하여 이 과정을 반복한다.
# 조건02) 반복문을 간단하게 하기 위해 무한루프를 사용한다.

def calc_prime_factorization(n):
    i = 2
    while i <= n:
        while True:
            if n % i == 0:
                print(i, end=" ") # i 는 n의 약수다.
                n = n // i
            else:
                break

        i += 1

if __name__ == "__main__":
    calc_prime_factorization(48)