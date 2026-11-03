from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return 'A'

#Jinja2
@app.route('/templates')
def home():
    return render_template('my_template_1.html', message='hi')
