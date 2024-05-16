from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_notification', methods=['GET', 'POST'])
def receive_notification():
    try:
        if request.method == 'GET':
            text_data = request.args.get('data', '')  # Extract text data from the query parameters
        elif request.method == 'POST':
            text_data = request.data.decode('utf-8')  # Extract text data from the request body
        else:
            return jsonify({"error": "Unsupported request method"}), 405
        
        # Handle the received text data here (e.g., log it)
        print("Received text data:", text_data)
        return jsonify({"message": "Notification received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

