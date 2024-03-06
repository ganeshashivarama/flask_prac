from flask import Flask, jsonify
import conf

app = Flask(__name__)

@app.route('/users/<int:user_id>', methods=['GET'])

def get_user(user_id):
    users = conf.USER_DETAIL
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User details not found!'}), conf.CODE_NOT_FOUND

if __name__ == '__main__':
    app.run(port=conf.USER_PORT)
