from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/input', methods=['POST'])
def get_input():
    # Receive hyperparameters from the user
    hyperparams = request.json
    
    # Forward hyperparameters to the processing service
    response = requests.post('http://processing_service:5001/process', json=hyperparams)
    return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
