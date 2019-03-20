## Flask Skeleton Program ##

from flask import Flask

# Flask 객체는 하나의 인자를 받는다.
# __name__ : 실행 중인 모듈의 이름
# 임의 문자열도 전달할 수 있다.
app = Flask(__name__)

# URL "/" 의 GET 요청에 대해 뷰 함수를 등록한다.
@app.route("/")
def helloworld():
    return "Hello World"