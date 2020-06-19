import pika
import json
import pickle
import numpy as np

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    with open('hw1.pkl', 'rb') as pkl_file:
        hw1 = pickle.load(pkl_file)

    params = request.json.get('params')

    return jsonify({'prediction': hw1.predict(np.array([params]))[0]})

if __name__ == '__main__':
    app.run('solution', 5000, debug=True)