from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Charlie'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Horrible day in Chichester!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avatar movie was so cool!'
        },
        {
            'author': {'username': 'Charlie'},
            'body': 'Flask seems pretty cool'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/')
@app.route('/secrets')
def secrets():
    password = '****'
    return render_template('secrets.html', password=password)