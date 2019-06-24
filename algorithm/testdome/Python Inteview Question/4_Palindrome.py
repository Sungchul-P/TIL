# 팔린드롬 : 앞으로 읽으나 뒤로 읽으나 같은 단어
    # 기러기, 오디오, stars, racecar 등..

# 대소문자 구분없이 결과를 반환해야 한다. 팔린드롬이면 True 반환.

# 문제 원형 #
'''
def is_palindrome(word):
    return None
    
print(is_palindrome('Deleveled'))
'''

def is_palindrome(word):
    word = word.lower()
    # 왼쪽과 오른쪽 끝의 글자 하나씩 비교
    for left in range(0, len(word)//2):
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    return True
    
print(is_palindrome('Deleveled'))