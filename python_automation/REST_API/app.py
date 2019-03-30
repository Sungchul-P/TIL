from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

# 사용자 모델을 정의한다.
users = [
    {
        'id': 1,
        'username': u'flask',
        'email': u'abc@xyz.com',
        'active': True
    },
    {
        'id': 2,
        'username': u'python',
        'email': u'py@py.org',
        'active': False
    }
]

# 사용자 ID를 기반으로 사용자 삭제
@app.route('/v1/users/<int:id>/', methods=['DELETE'])
def delete_user(id):
    user = [user for user in users if user['id'] == id]
    users.remove(user[0])
    return jsonify({}), 204

# 사용자 정보 수정
@app.route('/v1/users/<int:id>/', methods=['PUT'])
def update_user(id):
    user = [user for user in users if user['id'] == id]
    user[0]['username'] = request.json.get('username', user[0]['username'])
    user[0]['email'] = request.json.get('email', user[0]['email'])
    user[0]['active'] = request.json.get('active', user[0]['active'])
    return jsonify({'users': user[0]})

# 새로운 사용자 생성
@app.route('/v1/users/', methods=['POST'])
def create_user():
    if not request.json or not 'email' in request.json:
        abort(404)

    user_id = users[-1].get("id") + 1
    username = request.json.get('username')
    email = request.json.get('email')
    status = False
    user = {"id": user_id, "email": email,
            "username": username, "active": status}
    users.append(user)
    return jsonify({'user':user}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# ID를 기반으로 사용자 정보를 얻는다.
@app.route('/v1/users/<int:id>/', methods=['GET'])
def get_user(id):
    for user in users:
        if user.get("id") == id:
            return jsonify({'users': user})
    abort(404)

# 모든 사용자를 JSON 형식으로 반환한다.
@app.route('/v1/users/', methods=['GET'])
def get_users():
    return jsonify({'users': users})

@app.route('/')
def index():
    return "Hello, Python!"

if __name__ == '__main__':
    app.run(debug=True)