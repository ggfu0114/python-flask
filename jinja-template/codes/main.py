import os

from flask import Flask
from flask import render_template

project_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(project_dir, 'templates')

# Programmer can assign the specific folder as the template folder.
# template_dir = os.path.join(project_dir, 'my_templates_fd')

app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def hello():
    contact_list = [
        {'name': 'Alan', 'phone': '0935000001', 'email': 'alan@gmail.com'},
        {'name': 'Brian', 'phone': '0935000002', 'email': 'brian@gmail.com'},
        {'name': 'David', 'phone': '0935000003', 'email': 'david@gmail.com'}
    ]
    class_name = 'Python jinja'
    return render_template('index.html', contacts=contact_list, class_name=class_name)


if __name__ == '__main__':
    app.run(debug=True, port=8001)
