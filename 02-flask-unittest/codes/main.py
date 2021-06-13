from flask import Flask
import sys
from func import MathFunc
app = Flask(__name__)


@app.route('/')
def hello():
    mf = MathFunc()
    px,py = mf.get_random_point()
    res = mf.get_triangle_size((px,py))
    return f'Hello, gFu.\
            The size from p(0,0) to p({px},{py}) is {res}.'



if __name__ == '__main__':
    app.run(debug=True)
