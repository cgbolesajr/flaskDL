from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def main():
    return 'this is the index'


@app.route('/hello', methods=['POST'])
def hello():
    message = request.get_json(force=True)
    name = message['name']
    response = {'greeting': 'hello' +" " + name + '!'}
    return jsonify(response)


if __name__ == '__main__':
    print('Flask services is running')
    app.run()