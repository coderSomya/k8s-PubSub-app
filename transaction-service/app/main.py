from flask import Flask, request, jsonify
from consumer import consume_orders
from producer import produce_analytics, produce_notification
from database import store_transaction

app = Flask(__name__)

@app.route('/transaction', methods=['POST'])
def transaction():
    try:
       order = request.json
       store_transaction(order)
    #    produce_analytics(order)
    #    produce_notification(order)
       return jsonify({'status': 'transaction stored'}), 200
    except:
       return jsonify({'status': 'something went wrong while transacting'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

