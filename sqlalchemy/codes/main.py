import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(project_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def hello():
    users = User.query.all()
    class_name = 'Python sqlalchemy'
    return render_template('index.html', all_users=users, class_name=class_name)


if __name__ == '__main__':
    app.run(debug=True, port=8001)
