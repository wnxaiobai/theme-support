from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('user-map.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

