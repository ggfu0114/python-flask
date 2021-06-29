from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<div>Hello World, gFu.<div>"


if __name__ == '__main__':
    app.run(debug=True, port=8001)
