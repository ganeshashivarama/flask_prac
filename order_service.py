from flask import Flask, jsonify
import conf

app = Flask(__name__)
@app.route('/orders/<int:order_id>', methods=['GET'])

def get_order(order_id):
    orders = conf.ORDER_DETAIL
    order = orders.get(order_id)
    if order:
        return jsonify(order)
    else:
        return jsonify({'error': 'Order not found!'}), conf.CODE_NOT_FOUND
    
if __name__ == '__main__':
    app.run(port=conf.ORDER_PORT)