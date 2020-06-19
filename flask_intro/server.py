from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'hello {name}!'

@app.route('/add', methods=['POST'])
def add_func():
    num = request.json.get('num')
    if num > 10:
        return 'too much', 400
    return jsonify({'result': num + 1})

@app.route('/predict', methods=['POST'])
def predict():
    with open('hw1.pkl', 'rb') as pkl_file:
        hw1 = pickle.load(pkl_file)

    params = request.json.get('params')

    return jsonify({'prediction': hw1.predict(np.array([params]))[0]})

if __name__ == '__main__':
    app.run('localhost', 5000)