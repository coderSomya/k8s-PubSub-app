from flask import Flask, request, jsonify
from producer import produce_order

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def home():
    return jsonify({"msg": "ok"})

@app.route('/order', methods=['POST'])
def order():
    try:
        data = request.json
        produce_order(data)
        return jsonify({'status': 'order produced'}), 200
    except:
        return jsonify({'status': 'error while producing order'}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
        
