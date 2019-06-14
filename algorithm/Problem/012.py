# 012. 약수의 합 출력하기

# 조건 01) 주어진 숫자 n의 약수에는 1과 자기자신도 포함된다.
# 조건 02) 약수를 구할 때마다 하나의 변수에 더하여 저장한다.

def solve(n):
    total = 0
    i = 1
    while i <= n:
        if n % i == 0:
            total += i
        i += 1

    return total

if __name__ == "__main__":
    n = 20

    print("{}까지 약수의 합은 {}이다.".format(n, solve(n)))
