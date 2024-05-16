from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/receive_notification', methods=['GET','POST'])
def receive_notification():
    try:
        data = request.json  # Parse JSON data from the request
        # Handle the received JSON data here (e.g., log it)
        print("Received JSON data:", data)
        return jsonify({"message": "Notification received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

