from helloworld import app

# __init__에 정의된 프로그램을 Flask 내장 웹 서버를 이용해 기동시킨다.
if __name__ == "__main__":
    app.run(host="0.0.0.0")