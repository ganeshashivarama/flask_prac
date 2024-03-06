from flask import Flask, jsonify
import requests
import conf

app = Flask(__name__)

USER_SERVICE_URL = conf.USER_SERVICE_URL
ORDER_SERVICE_URL = conf.ORDER_SERVICE_URL

@app.route('/user_and_order/<int:user_id>/<int:order_id>', methods =['GET'])

def get_user_and_order(user_id, order_id):
    
    user_response = requests.get(USER_SERVICE_URL+str(user_id))
    #print(f"user_response: {user_response}")

    order_response = requests.get(ORDER_SERVICE_URL+str(order_id))
    #print(f"order_response: {order_response}")

    if user_response.status_code == conf.CODE_SUCCESS or order_response.status_code == conf.CODE_SUCCESS:
        return jsonify({
            'user': user_response.json(),
            'order': order_response.json()
        })
    else:
        return jsonify({'error': 'User and Order details not found!'}), conf.CODE_NOT_FOUND
    
if __name__ == '__main__':
    app.run(port=conf.GATEWAY_PORT)
