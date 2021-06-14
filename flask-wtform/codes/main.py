import os

from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SelectField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'This secret key is not for production.'


class Form(FlaskForm):
    name = StringField('name', validators=[DataRequired(message='Name is Null')])
    email = EmailField('Email', validators=[DataRequired(message='Email is Null')])
    gender = SelectField('Gender', choices=[('MALE', 'male'), ('FEMALE', 'female')])
    birth = DateField('Birth')
    description = TextAreaField('Description')
    photo = FileField('Photo', validators=[FileRequired()])


@app.route('/')
def hello():
    form = Form()

    return render_template('index.html', form=form)


@app.route('/save', methods=['POST'])
def upload():
    project_dir = os.path.abspath(os.path.dirname(__file__))
    photo_dir = os.path.join(project_dir, 'photo')
    form = Form()

    if form.validate_on_submit():
        f = form.photo.data
        photo_file_path = os.path.join(photo_dir, 'upload_photo.jpg')
        f.save(photo_file_path)

        print(f'Hi, {form.name.data}.')
        print(f'We have received your data.')
        print(f'The photo is saved to {photo_file_path}.')

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8001)
