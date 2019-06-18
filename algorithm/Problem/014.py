# 014. 재귀 호출을 사용하여 최대공약수 구하기

# 유클리드 호제법 사용
# 조건01) 반복문의 코드 대신 재귀 호출로 작성한다.
# 조건02) 재귀 호출의 종료 조건은 작은 수가 0이 될 때 종료한다.

def gcd_solve(p, q):
    if p > q:
        a = p
        b = q
    else:
        a = q
        b = p

    if b == 0:
        return a

    return gcd_solve(b, a % b)

if __name__ == "__main__":
    r = gcd_solve(24, 64)
    print("24와 64의 최대공약수 : {}".format(r))