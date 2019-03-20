class CodeConverter:
    regex = r'\d{5}'
    
    # regex에 해당하는 값이면 value에 문자열로 전달
    def to_python(self, value):
        print("to_python() : ", type(value), value)
        return int(value) # 숫자로 형변환하여 반환
