from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/new')
def add_score():
    return "scores"


if __name__ == '__main__':
    app.run(debug=True)
