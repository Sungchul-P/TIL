# 010. 약수 구하기

# 조건 01) n의 약수를 구하기 위해서 2부터 n의 제곱근까지만 탐색한다.
# 조건 02) 소수가 아닌 경우에는 약수를 구해야 하기 때문에 이전의 소수를 구하는 문제와는 달리 break문을 사용할 수 없다.
# 조건 03) 소수인지 아닌지를 저장해두기 위해 플래그 변수를 사용한다.

# 소수 유무를 체크하는 함수
# 소수인 경우 True, 아니면 False
def isPrime(k):
    i = 2
    flag = True
    while i < k:
        if k % i == 0:
            # print("약수 : {}".format(i)) # i는 k의 약수
            flag = False
        i += 1
    return flag

def solve(n):
    i = 1
    while i <= (n // 2):
        if i > 1 and isPrime(i) == True:
            print("소수 : {}".format(i))
        else:
            if n % i == 0:
                print("> 약수 : {}".format(i))
        i += 1

if __name__ == "__main__":
    n = int(input("입력: "))
    solve(n)