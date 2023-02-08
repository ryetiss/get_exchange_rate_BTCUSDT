# This script runs flask app on host getting content from file.
from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    with open('price_change.txt', 'r') as f:
        content = f.read()
    return Response(content, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
