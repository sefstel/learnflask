from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Sefstel"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Какая гадость эта ваша заливная рыба'
         },
        {
            'author': {'username': 'Ипполит'},
            'body': 'The advengers movie was so cool'
         }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
