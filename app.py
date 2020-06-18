from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def data():
    data = {
        "Hello": os.environ.get("NAME", "World")
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000, debug=True)
