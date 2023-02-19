from flask import Flask
import os

print('hello world')


app = Flask(__name__)

@app.route('/')
def home2():
    return "Hello"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)